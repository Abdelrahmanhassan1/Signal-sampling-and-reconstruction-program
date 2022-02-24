# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\task2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #A9A9A9;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.browse_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout_4.addWidget(self.browse_button)
        self.show_dotted_reconstructed_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.show_dotted_reconstructed_button.setFont(font)
        self.show_dotted_reconstructed_button.setObjectName("show_dotted_reconstructed_button")
        self.horizontalLayout_4.addWidget(self.show_dotted_reconstructed_button)
        self.show_hide_reconstructed_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.show_hide_reconstructed_button.setFont(font)
        self.show_hide_reconstructed_button.setObjectName("show_hide_reconstructed_button")
        self.horizontalLayout_4.addWidget(self.show_hide_reconstructed_button)
        self.reset_button_fo_main = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reset_button_fo_main.setFont(font)
        self.reset_button_fo_main.setObjectName("reset_button_fo_main")
        self.horizontalLayout_4.addWidget(self.reset_button_fo_main)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.splitter_4 = QtWidgets.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: #A9A9A9;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.sampling_slider = QtWidgets.QSlider(self.layoutWidget)
        self.sampling_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sampling_slider.setObjectName("sampling_slider")
        self.verticalLayout.addWidget(self.sampling_slider)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: #A9A9A9;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.saved_signals_box = QtWidgets.QComboBox(self.layoutWidget_2)
        self.saved_signals_box.setObjectName("saved_signals_box")
        self.verticalLayout_7.addWidget(self.saved_signals_box)
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.splitter_5 = QtWidgets.QSplitter(self.tab)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #A9A9A9;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #A9A9A9;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.original_signal_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.original_signal_layout.setContentsMargins(0, 0, 0, 0)
        self.original_signal_layout.setObjectName("original_signal_layout")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.reconstructed_signal_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.reconstructed_signal_layout.setContentsMargins(0, 0, 0, 0)
        self.reconstructed_signal_layout.setObjectName("reconstructed_signal_layout")
        self.verticalLayout_8.addWidget(self.splitter_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.splitter_6 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_6)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #A9A9A9;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.phase_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.phase_label.setFont(font)
        self.phase_label.setAlignment(QtCore.Qt.AlignCenter)
        self.phase_label.setObjectName("phase_label")
        self.horizontalLayout_3.addWidget(self.phase_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.phaseslider = QtWidgets.QSlider(self.layoutWidget3)
        self.phaseslider.setOrientation(QtCore.Qt.Horizontal)
        self.phaseslider.setObjectName("phaseslider")
        self.verticalLayout_6.addWidget(self.phaseslider)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: #A9A9A9;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.mag_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mag_label.setFont(font)
        self.mag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mag_label.setObjectName("mag_label")
        self.horizontalLayout_2.addWidget(self.mag_label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.magslider = QtWidgets.QSlider(self.layoutWidget3)
        self.magslider.setOrientation(QtCore.Qt.Horizontal)
        self.magslider.setObjectName("magslider")
        self.verticalLayout_5.addWidget(self.magslider)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: #A9A9A9;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.freq_label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.freq_label.setFont(font)
        self.freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.freq_label.setObjectName("freq_label")
        self.horizontalLayout.addWidget(self.freq_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.freqslider = QtWidgets.QSlider(self.layoutWidget3)
        self.freqslider.setOrientation(QtCore.Qt.Horizontal)
        self.freqslider.setObjectName("freqslider")
        self.verticalLayout_4.addWidget(self.freqslider)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget4 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: #A9A9A9;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.added_signals_box = QtWidgets.QComboBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.added_signals_box.setFont(font)
        self.added_signals_box.setObjectName("added_signals_box")
        self.verticalLayout_3.addWidget(self.added_signals_box)
        self.verticalLayout_12.addWidget(self.splitter_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.draw_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.draw_button.setFont(font)
        self.draw_button.setObjectName("draw_button")
        self.horizontalLayout_7.addWidget(self.draw_button)
        self.delete_from_graph = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.delete_from_graph.setFont(font)
        self.delete_from_graph.setObjectName("delete_from_graph")
        self.horizontalLayout_7.addWidget(self.delete_from_graph)
        self.move_to_main = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.move_to_main.setFont(font)
        self.move_to_main.setObjectName("move_to_main")
        self.horizontalLayout_7.addWidget(self.move_to_main)
        self.reset_button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_7.addWidget(self.reset_button)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_6)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.BasisFunctionLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.BasisFunctionLayout.setContentsMargins(0, 0, 0, 0)
        self.BasisFunctionLayout.setObjectName("BasisFunctionLayout")
        self.verticalLayout_13.addWidget(self.splitter_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1231, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sampling Studio"))
        self.label.setText(_translate("MainWindow", "Signal Sampling and Reconstruction"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.show_dotted_reconstructed_button.setText(_translate("MainWindow", "Show Dotted reconstructed signal"))
        self.show_hide_reconstructed_button.setText(_translate("MainWindow", "Show/Hide reconstructed"))
        self.reset_button_fo_main.setText(_translate("MainWindow", "RESET"))
        self.label_5.setText(_translate("MainWindow", "Sampling Signal Frequency: (0 ~ 3fmax)"))
        self.label_15.setText(_translate("MainWindow", "Saved Signals"))
        self.label_3.setText(_translate("MainWindow", "Original Signal "))
        self.label_2.setText(_translate("MainWindow", "Reconstructed Signal "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Signal Sampling and Reconstruction"))
        self.label_13.setText(_translate("MainWindow", "Phase:"))
        self.phase_label.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Magnitude:"))
        self.mag_label.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "Frequency:"))
        self.freq_label.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "Added Signals"))
        self.draw_button.setText(_translate("MainWindow", "Add To Graph"))
        self.delete_from_graph.setText(_translate("MainWindow", "Delete from graph"))
        self.move_to_main.setText(_translate("MainWindow", "Move To The Main Graph"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Signal Composer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
