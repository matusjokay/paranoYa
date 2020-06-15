from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.GenerateWindow import Ui_GenerateWindow
import src.app.main_window


class OpenGen:
    def open_gen(self):
        mw = src.app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_GenerateWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
