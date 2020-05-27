from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.ResultsWindow import Ui_ResultsWindow
from gui.generated.SummaryWindow import Ui_SummaryWindow
import app.main_window, app.summary_window


class ResultsWindow:
    def results_window(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_ResultsWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
        mw.ui.pushButton.clicked.connect(app.summary_window.SummaryWindow.summary_window)

