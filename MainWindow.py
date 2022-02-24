from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import pathlib
import numpy as np
from matplotlib.figure import Figure
import statistics
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.figure import Figure
from PyPDF2 import PdfFileMerger, PdfFileReader
import pdfkit
from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_MainWindow
from signal_sampling import *

MainWindow



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


