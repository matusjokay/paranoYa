from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.LoadTestWindow import Ui_LoadTestWindow
import app.main_window


class LoadTests:
    def load_tests(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_LoadTestWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
