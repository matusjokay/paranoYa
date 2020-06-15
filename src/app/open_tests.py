from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.TestingWindow import Ui_TestingWindow
import src.app.main_window
import src.tests.NIST.test


class OpenTests:
    def open_tests(self):
        mw = src.app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_TestingWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()
        mw.loaded_test_set = [1, 2, 3, 4, 5, 6, 7]
        mw.files = ['input.txt']

        src.tests.NIST.test.main(mw.files, mw.loaded_test_set)
