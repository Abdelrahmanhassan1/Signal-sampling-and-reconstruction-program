import math
import sys
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from numpy.fft import fftfreq, fft
from scipy import signal
from scipy import fftpack
from scipy import interpolate
from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signal Composer
        #############################################
        self.range = 1
        self.time_range = np.arange(0, self.range, 0.001)
        self.saved_signals_dict = {}
        self.added_signals_dict = {}
        self.signals_summation = []
        self.full_signal = np.zeros(5000)
        self.time_data_from_imported_file = []
        self.amplitude_data_from_imported_file = []
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
        self.ui.reset_button_fo_main.clicked.connect(self.reset)
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
            self.sine_wave_figure_axes.plot(self.time_range, self.full_signal)
            self.sine_wave_figure_axes.set_xlabel('Time')
            self.sine_wave_figure_axes.set_ylabel('Magnitude')
            self.sine_wave_figure_axes.set_title('Sinusoidal Signal')
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
                sine_wave_figure_axes = self.sine_wave_figure.gca()
                sine_wave_figure_axes.cla()
                sine_wave_figure_axes.grid(True)
                sine_wave_figure_axes.set_facecolor((1, 1, 1))
                sine_wave_figure_axes.plot(self.time_range, self.full_signal)
                sine_wave_figure_axes.set_xlabel('Time')
                sine_wave_figure_axes.set_ylabel('Magnitude')
                sine_wave_figure_axes.set_title('Sinusoidal Signal')
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
        sine_wave = mag * np.sin((2 * np.pi * freq * self.time_range) + ((np.pi / 180) * phase))
        return sine_wave

    def show_empty_sine_graph(self):
        self.sine_wave_figure_axes = self.sine_wave_figure.gca()
        self.sine_wave_figure_axes.cla()
        self.sine_wave_figure_axes.grid(True)
        self.sine_wave_figure_axes.set_facecolor((1, 1, 1))

    ############################################################
    # Signal Composer

    ############################################################
    # Main Window
    def browse_file(self):
        try:
            file_name = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
            data_frame = pd.read_csv(file_name)
            self.time_data_from_imported_file = data_frame.iloc[:, 0].values
            # print(self.first_col)
            self.amplitude_data_from_imported_file = data_frame.iloc[:, 1].values
            # print(self.second_col)
            self.calculate_max_frequency(self.time_data_from_imported_file, self.amplitude_data_from_imported_file)
            self.flag2 = False
            self.show_original_signal()
        except Exception as e:
            print(e)

    def show_original_signal(self):
        try:
            self.composer_flag = False
            self.saved_signals_flag = False
            self.clear_reconstructed_figure()
            main_graph_axis = self.original_signal.gca()
            main_graph_axis.cla()
            main_graph_axis.grid(True)
            main_graph_axis.set_facecolor((1, 1, 1))
            main_graph_axis.plot(self.time_data_from_imported_file, self.amplitude_data_from_imported_file)
            main_graph_axis.set_xlabel('Time')
            main_graph_axis.set_ylabel('Magnitude')
            main_graph_axis.set_title('Original Signal')
            main_graph_axis.legend(['Original Signal'])
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def saved_signals(self):
        self.saved_signals_dict['2sin(2)Hz + 2sin(6)Hz'] = self.create_sinusoidal(2, 6, 0) + self.create_sinusoidal(2,2,0)

        self.saved_signals_dict['2sin(5)Hz + 2sin(8)Hz'] = self.create_sinusoidal(2, 5, 0)  + self.create_sinusoidal(2, 8, 0)

        self.saved_signals_dict['sin(1)Hz + 2sin(6)Hz'] = self.create_sinusoidal(1, 1, 0) + self.create_sinusoidal(2, 6, 0)

        self.saved_signals_dict['cos(1)Hz + 2cos(8)Hz'] = self.create_sinusoidal(1, 1, 90) + self.create_sinusoidal(2, 8, 90)

        self.ui.saved_signals_box.addItem("")
        for key in self.saved_signals_dict.keys():
            self.ui.saved_signals_box.addItem(key)

    def show_reconstructed_signal(self):
        try:
            self.flag_check()
            # sample_points = signal.resample(self.second_column_used, self.sampling_slider_value, self.first_column_used)
            # # Resample x to num samples using Fourier method along the given axis
            # x_new = np.linspace(min(self.first_column_used), max(self.first_column_used), self.sampling_slider_value)
            # # new x values for the sampled points
            # interpolation_function = interpolate.interp1d(self.time_domain_sample_points, self.amplitude_values_sample_points, kind='cubic')
            # time_values_interpolated = np.arange(min(self.time_domain_sample_points), max(self.time_domain_sample_points), 0.01)
            # amplitude_values_interpolated = interpolation_function(time_values_interpolated)
            sample_time = 1 / self.sampling_slider_value
            calculated_y_value_interpolated = 0
            for sample_index in range(0, len(self.time_domain_sample_points)):
                calculated_y_value_interpolated += self.amplitude_values_sample_points[sample_index] * np.sinc(
                    (self.time_array_values - sample_time * (sample_index)) / sample_time)
            print(calculated_y_value_interpolated)

            # print(xr)
            axes = self.reconstructed_signal.gca()
            axes.cla()
            axes.grid(True)
            axes.set_facecolor((1, 1, 1))
            axes.plot(self.time_array_values, calculated_y_value_interpolated )
            # axes.plot(self.time_array_values, calculated_y_value_interpolated)
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
            interpolation_function = interpolate.interp1d(self.time_domain_sample_points, self.amplitude_values_sample_points, kind='cubic')
            time_values_interpolated = np.arange(min(self.time_domain_sample_points), max(self.time_domain_sample_points), 0.01)
            amplitude_values_interpolated = interpolation_function(time_values_interpolated)
            Main_graph_axis = self.original_signal.gca()
            Main_graph_axis.cla()
            Main_graph_axis.grid(True)
            Main_graph_axis.set_facecolor((1, 1, 1))
            Main_graph_axis.plot(self.time_array_values, self.amplitude_array_values, label="Original Signal")
            Main_graph_axis.set_xlabel('Time')
            Main_graph_axis.set_ylabel('Magnitude')
            Main_graph_axis.set_title('Original Signal')
            Main_graph_axis.plot(time_values_interpolated, amplitude_values_interpolated, "--", c="red", label='Dotted Reconstructed Signal')
            Main_graph_axis.legend()
            self.original_signal_canvas.draw()
            self.original_signal_canvas.flush_events()
        except Exception as e:
            print(e)

    def show_sampling_points(self):
        try:
            self.flag_check()
            # sample_time = 1 / self.sampling_slider_value
            self.amplitude_values_sample_points = []
            self.time_domain_sample_points = []
            # Time_Values = []
            self.Samples = []
            Step_in_index = int(np.ceil(len(self.time_array_values)) / (max(self.time_array_values) * self.sampling_slider_value + 0.0001 ))
            for index in range(0, len(self.time_array_values), Step_in_index):
                self.amplitude_values_sample_points.append(self.amplitude_array_values[index])
                self.time_domain_sample_points.append(self.time_array_values[index])

            # self.amplitude_values_sample_points, self.time_domain_sample_points = signal.resample(self.amplitude_array_values, self.sampling_slider_value, t=self.time_array_values)
            # x_new = np.linspace(min(self.time_array_values), max(self.time_array_values), self.sampling_slider_value)
            # sample_time = 1 / self.sampling_slider_value
            # print(sample_time)
            # for _ in range(len(self.time_array_values)/sample_time):
            main_graph_axis = self.original_signal.gca()
            main_graph_axis.cla()
            main_graph_axis.grid(True)
            main_graph_axis.set_facecolor((1, 1, 1))
            main_graph_axis.plot(self.time_array_values, self.amplitude_array_values, label="Original Signal")
            main_graph_axis.scatter(self.time_domain_sample_points, self.amplitude_values_sample_points, c="red", label='Sampling Points')
            main_graph_axis.set_xlabel('Time')
            main_graph_axis.set_ylabel('Magnitude')
            main_graph_axis.set_title('Original Signal')
            main_graph_axis.legend()
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
                main_graph_axis = self.original_signal.gca()
                main_graph_axis.cla()
                main_graph_axis.grid(True)
                main_graph_axis.set_facecolor((1, 1, 1))
                main_graph_axis.plot(self.time_range, self.saved_signals_dict[self.signal_name])
                main_graph_axis.set_xlabel('Time')
                main_graph_axis.set_ylabel('Magnitude')
                main_graph_axis.set_title(self.signal_name)
                self.original_signal_canvas.draw()
                self.original_signal_canvas.flush_events()
                self.calculate_max_frequency(self.time_range, self.saved_signals_dict[self.signal_name])
            # print(self.saved_signals_flag)
            # print(self.max_frequency)
        except Exception as e:
            print(e)

    def calculate_max_frequency(self, first_column, second_column):
        # Calculating the maximum frequency
        self.TimeAxis = first_column
        self.amplitude = second_column
        self.sample_rate = int(len(self.TimeAxis) / max(self.TimeAxis))
        self.Power = list(np.abs(fft(self.amplitude)))
        self.FreQList = []
        self.Freq = list(np.abs(fftfreq(len(self.TimeAxis), 1 / self.sample_rate)))
        for index in range(1, len(self.Freq) // 2):
            if (1e-1 < self.Power[index] - self.Power[index - 1]) and (
                    1e-1 < self.Power[index] - self.Power[index + 1]):
                self.FreQList.append(self.Freq[index])
        ##print(int(self.FreQList[-1]))
        return int(self.FreQList[-1])

    def move_to_main_graph(self):
        try:
            main_graph_axis = self.original_signal.gca()
            main_graph_axis.cla()
            main_graph_axis.grid(True)
            main_graph_axis.set_facecolor((1, 1, 1))
            main_graph_axis.plot(self.time_range, self.full_signal)
            main_graph_axis.set_xlabel('Time')
            main_graph_axis.set_ylabel('Magnitude')
            main_graph_axis.set_title('Sinusoidal Signal')
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
            self.time_array_values = self.time_range
            self.amplitude_array_values = self.saved_signals_dict[self.signal_name]
        elif self.composer_flag:
            self.time_array_values = self.time_range
            self.amplitude_array_values = self.full_signal
        else:
            self.time_array_values = self.time_data_from_imported_file
            self.amplitude_array_values = self.amplitude_data_from_imported_file

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

    def reset(self):
        self.clear_original_figure()
        self.clear_reconstructed_figure()
        self.time_data_from_imported_file = []
        self.amplitude_data_from_imported_file = []

    # Main Window
    ############################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

