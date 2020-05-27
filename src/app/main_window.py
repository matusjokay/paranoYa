import sys

sys.path.append(".")

from gui.generated.AddTestWindow import Ui_AddTestWindow
from PyQt5 import QtCore, QtWidgets
from gui.generated.MainWindow import Ui_MainWindow
import app.add_tests, app.load_tests, app.open_tests, app.generate_window, app.sequence_window


class MainWindow:
    __instance = None

    @staticmethod
    def getInstance():
        if MainWindow.__instance is None:
            MainWindow()
        return MainWindow.__instance

    def __init__(self):
        if MainWindow.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MainWindow.__instance = self


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.window = QtWidgets.QMainWindow()
    mw.ui = Ui_MainWindow()
    mw.ui.setupUi(mw.window)
    mw.window.show()

    mw.ui.pushButton.clicked.connect(app.load_tests.LoadTests.load_tests)
    mw.ui.pushButton_2.clicked.connect(app.add_tests.AddTest.open_add_test)
    mw.ui.pushButton_3.clicked.connect(app.open_tests.OpenTests.open_tests)
    mw.ui.pushButton_4.clicked.connect(app.sequence_window.SequenceWindow.sequence_window)
    mw.ui.pushButton_5.clicked.connect(app.generate_window.OpenGen.open_gen)

    sys.exit(application.exec_())
