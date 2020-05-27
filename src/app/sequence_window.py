from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.SequenceWindow import Ui_SequenceWindow
import app.main_window


class SequenceWindow:
    def sequence_window(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_SequenceWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
