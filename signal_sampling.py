import sys
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from scipy import signal
from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signal Composer
        #############################################
        self.range = 5
        self.time_range = np.arange(0, self.range, 0.001)
        self.saved_signals_dict = {}
        self.added_signals_dict = {}
        self.signals_summation = []
        self.full_signal = np.zeros(5000)
        self.first_col = []
        self.second_col = []
        self.saved_signals_flag = False
        self.composer_flag = False

        self.sine_wave_figure = Figure()
        self.sine_wave_canvas = FigureCanvas(self.sine_wave_figure)
        self.ui.BasisFunctionLayout.addWidget(self.sine_wave_canvas)

        empty_list = []
        self.sinusoidal_wave_summation = np.empty(empty_list)
        self.set_slider_ranges()
        self.saved_signals()

        # Sliders Moved:
        self.ui.phaseslider.valueChanged.connect(self.read_slider_values)
        self.ui.freqslider.valueChanged.connect(self.read_slider_values)
        self.ui.magslider.valueChanged.connect(self.read_slider_values)

        # Buttons:
        self.ui.reset_button.clicked.connect(self.show_initialized_graph)
        self.ui.draw_button.clicked.connect(self.draw_sine_wave)
        # self.ui.add_to_combo_box.clicked.connect(self.add_signal_to_combo_box)
        # self.ui.delete_from_combo_box.clicked.connect(self.delete_signal_from_combo_box)
        self.ui.delete_from_graph.clicked.connect(self.delete_signal_from_graph)
        self.ui.move_to_main.clicked.connect(self.move_to_main_graph)



        #############################################
        # Signal Composer

        ############################################################
        # Main Window
        self.original_signal = Figure()
        self.original_signal_canvas = FigureCanvas(self.original_signal)
        self.ui.original_signal_layout.addWidget(self.original_signal_canvas)

        self.reconstructed_signal = Figure()
        self.reconstructed_signal_canvas = FigureCanvas(self.reconstructed_signal)
        self.ui.reconstructed_signal_layout.addWidget(self.reconstructed_signal_canvas)

        self.ui.browse_button.clicked.connect(self.browse_file)
        self.ui.show_original_button.clicked.connect(self.show_original_signal)
        self.ui.show_hide_reconstructed_button.clicked.connect(self.hide_reconstructed)
        # self.ui.show_sampling_points.clicked.connect(self.show_sampling_points)
        self.ui.show_dotted_reconstructed_button.clicked.connect(self.show_dotted_reconstructed_signal)
        self.ui.sampling_slider.valueChanged.connect(self.sampling_slider_moved)
        self.ui.saved_signals_box.currentIndexChanged.connect(self.draw_from_saved_functions)

        # Main Window
        ############################################################

    #############################################
    # Signal Composer

    def set_slider_ranges(self):
        self.ui.phaseslider.setMinimum(0)
        self.ui.phaseslider.setMaximum(360)

        self.ui.magslider.setMinimum(1)
        self.ui.magslider.setMaximum(20)

        self.ui.freqslider.setMinimum(1)
        self.ui.freqslider.setMaximum(30)

    def read_slider_values(self):
        self.phase = self.ui.phaseslider.value()
        self.magnitude = self.ui.magslider.value()
        self.frequency = self.ui.freqslider.value()
        self.ui.freq_label.setText(str(self.frequency))
        self.ui.mag_label.setText(str(self.magnitude))
        self.ui.phase_label.setText(str(self.phase))

    def draw_sine_wave(self):
        try:
            self.read_slider_values()
            self.sine_wave = self.create_sinusoidal(self.magnitude, self.frequency, self.phase)
            self.full_signal += self.sine_wave
            self.show_empty_sine_graph()
            self.axes.plot(self.time_range, self.full_signal)
            self.axes.set_xlabel('Time')
            self.axes.set_ylabel('Magnitude')
            self.axes.set_title('Sinusoidal Signal')
            self.sine_wave_canvas.draw()
            self.sine_wave_canvas.flush_events()
            self.add_signal_to_combo_box()
        except Exception as e:
            print(e)

    def add_signal_to_combo_box(self):
        try:
            signal_name = f"sinusoidal wave: {self.magnitude}Amp,{self.frequency}HZ,and {self.phase}˚ phase"
            check_exist_index = self.ui.added_signals_box.findText(signal_name)
            # print(check_exist_index)
            if check_exist_index == -1:
                self.added_signals_dict[signal_name] = self.create_sinusoidal(self.magnitude, self.frequency,self.phase)
                # print(self.added_signals_dict)
                self.ui.added_signals_box.addItem(signal_name)
            else:
                print("Signal is already added")
        except Exception as e:
            print(e)

    def delete_signal_from_combo_box(self):
        try:
            signal_name = self.ui.added_signals_box.currentText()
            signal_index = self.ui.added_signals_box.currentIndex()
            # print(signal_name)
            del self.added_signals_dict[signal_name]
            # print(self.added_signals_dict)
            self.ui.added_signals_box.removeItem(signal_index)
        except Exception as e:
            print(e)

    def delete_signal_from_graph(self):
        try:
            signal_name = self.ui.added_signals_box.currentText()
            self.full_signal -= self.added_signals_dict[signal_name]
            self.delete_signal_from_combo_box()
            if self.ui.added_signals_box.count() == 0:
                self.show_initialized_graph()
            else:
                # print(self.full_signal)
                axes = self.sine_wave_figure.gca()
                axes.cla()
                axes.grid(True)
                axes.set_facecolor((1, 1, 1))
                axes.plot(self.time_range, self.full_signal)
                axes.set_xlabel('Time')
                axes.set_ylabel('Magnitude')
                axes.set_title('Sinusoidal Signal')
                self.sine_wave_canvas.draw()
                self.sine_wave_canvas.flush_events()

        except Exception as e:
            print(e)

    def show_initialized_graph(self):
        self.ui.freqslider.setSliderPosition(0)
        self.ui.magslider.setSliderPosition(1)
        self.ui.phaseslider.setSliderPosition(0)
        self.ui.added_signals_box.clear()
        self.added_signals_dict = {}
        self.show_empty_sine_graph()
        self.sine_wave_canvas.draw()
        self.sine_wave_canvas.flush_events()

    def create_sinusoidal(self, mag, freq, phase):
        sine_wave = mag * np.sin((2 * np.pi * freq * self.time_range / 5) + ((np.pi / 180) * phase))
        return sine_wave

    def show_empty_sine_graph(self):
        self.axes = self.sine_wave_figure.gca()
        self.axes.cla()
        self.axes.grid(True)
        self.axes.set_facecolor((1, 1, 1))

    ############################################################
    # Signal Composer

    ############################################################
    # Main Window
    def browse_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
            data_frame = pd.read_csv(file_name)
            self.first_col = data_frame.iloc[:, 0].values
            # print(self.first_col)
            self.second_col = data_frame.iloc[:, 1].values
            # print(self.second_col)
            self.calculate_max_frequency(self.first_col, self.second_col)
            self.flag2 = False
        except Exception as e:
            print(e)

    def show_original_signal(self):
        try:
            self.composer_flag = False
            self.saved_signals_flag = False
            self.clear_reconstructed_figure()
            axes = self.original_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(self.first_col, self.second_col)
            axes.set_xlabel('Time')
            axes.set_ylabel('Magnitude')
            axes.set_title('Original Signal')
            axes.legend(['Original Signal'])
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def saved_signals(self):
        self.saved_signals_dict['2sin(2)Hz + 2sin(6)Hz'] = self.create_sinusoidal(2, 2, 0) \
                                                           + self.create_sinusoidal(2, 6, 0)

        self.saved_signals_dict['2sin(5)Hz + 2sin(8)Hz'] = self.create_sinusoidal(2, 5, 0) \
                                                           + self.create_sinusoidal(2, 8, 0)

        self.saved_signals_dict['sin(1)Hz + 2sin(6)Hz'] = self.create_sinusoidal(1, 1, 0) + self.create_sinusoidal(2, 6,
                                                                                                                   0)

        self.saved_signals_dict['cos(1)Hz + 2cos(8)Hz'] = self.create_sinusoidal(1, 1, 90) + self.create_sinusoidal(2,
                                                                                                                    8,
                                                                                                                    90)

        self.ui.saved_signals_box.addItem("")
        for key in self.saved_signals_dict.keys():
            self.ui.saved_signals_box.addItem(key)

    def show_reconstructed_signal(self):
        try:
            self.flag_check()
            sample_points = signal.resample(self.second_column_used, self.sampling_slider_value)
            # Resample x to num samples using Fourier method along the given axis
            x_new = np.linspace(min(self.first_column_used), max(self.first_column_used), self.sampling_slider_value)
            # new x values for the sampled points
            axes = self.reconstructed_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(x_new, sample_points)
            axes.set_xlabel('Time')
            axes.set_ylabel('Magnitude')
            axes.set_title('Reconstructed Signal')
            self.reconstructed_signal_canvas.draw()
            self.reconstructed_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def show_dotted_reconstructed_signal(self):
        try:
            self.flag_check()
            sample_points = signal.resample(self.second_column_used, self.sampling_slider_value)
            x_new = np.linspace(min(self.first_column_used), max(self.first_column_used), self.sampling_slider_value)
            axes = self.original_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(self.first_column_used, self.second_column_used, label="Original Signal")
            axes.set_xlabel('Time')
            axes.set_ylabel('Magnitude')
            axes.set_title('Original Signal')
            axes.plot(x_new, sample_points, "--", c="red", label='Dotted Reconstructed Signal')
            axes.legend()
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def show_sampling_points(self):
        try:
            self.flag_check()
            sample_points = signal.resample(self.second_column_used, self.sampling_slider_value)
            x_new = np.linspace(min(self.first_column_used), max(self.first_column_used), self.sampling_slider_value)
            axes = self.original_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(self.first_column_used, self.second_column_used, label="Original Signal")
            axes.scatter(x_new, sample_points, c="red", label='Sampling Points')
            axes.set_xlabel('Time')
            axes.set_ylabel('Magnitude')
            axes.set_title('Original Signal')
            axes.legend()
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def set_freq_slider_range(self):
        self.ui.sampling_slider.setMinimum(0)
        self.ui.sampling_slider.setMaximum(int(self.max_frequency * 3))

    def sampling_slider_moved(self):
        self.sampling_slider_value = self.ui.sampling_slider.value()
        self.show_sampling_points()
        self.show_reconstructed_signal()

    def draw_from_saved_functions(self):
        try:
            self.composer_flag = False
            self.signal_name = self.ui.saved_signals_box.currentText()
            if self.signal_name == "":
                self.saved_signals_flag = False
                self.clear_reconstructed_figure()
                self.clear_original_figure()
            else:
                self.saved_signals_flag = True
                axes = self.original_signal.gca()
                axes.cla()
                axes.grid(True)
                axes.set_facecolor((1, 1, 1))
                axes.plot(self.time_range, self.saved_signals_dict[self.signal_name])
                axes.set_xlabel('Time')
                axes.set_ylabel('Magnitude')
                axes.set_title(self.signal_name)
                self.original_signal_canvas.draw()
                self.original_signal_canvas.flush_events()
                self.calculate_max_frequency(self.time_range, self.saved_signals_dict[self.signal_name])
            print(self.saved_signals_flag)
            print(self.max_frequency)
        except Exception as e:
            print(e)

    def calculate_max_frequency(self, first_column, second_column):
        # Calculating the maximum frequency
        if max(first_column) == max(self.time_range):
            time_step = 3e-5
        else:
            time_step = (max(first_column) - min(first_column)) / len(first_column)
        spectrum = np.fft.fft(second_column)
        freq_range = np.fft.fftfreq(len(spectrum))
        threshold = 0.5 * max(abs(spectrum))
        mask = abs(spectrum) > threshold
        peaks = freq_range[mask]
        peaks = abs(peaks)
        self.max_frequency = max(peaks) / time_step
        print(self.max_frequency)
        self.set_freq_slider_range()

    def move_to_main_graph(self):
        try:
            axes = self.original_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(self.time_range, self.full_signal)
            axes.set_xlabel('Time')
            axes.set_ylabel('Magnitude')
            axes.set_title('Sinusoidal Signal')
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
            self.calculate_max_frequency(self.time_range, self.full_signal)
            self.composer_flag = True
            self.show_initialized_graph()
            self.ui.tabWidget.setCurrentIndex(0)
        except Exception as e:
            print(e)

    def flag_check(self):
        if self.saved_signals_flag:
            self.first_column_used = self.time_range
            self.second_column_used = self.saved_signals_dict[self.signal_name]
        elif self.composer_flag:
            self.first_column_used = self.time_range
            self.second_column_used = self.full_signal
        else:
            self.first_column_used = self.first_col
            self.second_column_used = self.second_col

    def hide_reconstructed(self):
        try:
            self.reconstructed_signal.set_visible(not self.reconstructed_signal.get_visible())
            self.reconstructed_signal_canvas.draw()
            self.reconstructed_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def clear_original_figure(self):
        self.original_signal.clear()
        self.original_signal_canvas.draw()
        self.original_signal_canvas.flush_events()

    def clear_reconstructed_figure(self):
        self.reconstructed_signal.clear()
        self.reconstructed_signal_canvas.draw()
        self.reconstructed_signal_canvas.flush_events()

    # Main Window
    ############################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

