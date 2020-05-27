from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.TestingWindow import Ui_TestingWindow
import app.main_window


class OpenTests:
    def open_tests(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_TestingWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
