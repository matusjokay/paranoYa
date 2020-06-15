from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.ResultsWindow import Ui_ResultsWindow
from src.gui.generated.SummaryWindow import Ui_SummaryWindow
import src.app.main_window, src.app.summary_window


class ResultsWindow:
    def results_window(self):
        mw = src.app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_ResultsWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
        mw.ui.pushButton.clicked.connect(src.app.summary_window.SummaryWindow.summary_window)

