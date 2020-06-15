from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.SummaryWindow import Ui_SummaryWindow
import src.app.main_window


class SummaryWindow:
    def summary_window(self):
        mw = src.app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_SummaryWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
