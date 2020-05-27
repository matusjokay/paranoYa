from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.GenerateWindow import Ui_GenerateWindow
import app.main_window


class OpenGen:
    def open_gen(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_GenerateWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
