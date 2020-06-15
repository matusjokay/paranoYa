import sys

sys.path.append(".")

from src.gui.generated.AddTestWindow import Ui_AddTestWindow
from PyQt5 import QtCore, QtWidgets
from src.gui.generated.MainWindow import Ui_MainWindow
import src.app.add_tests, src.app.load_tests, src.app.open_tests, src.app.generate_window, src.app.sequence_window


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

    mw.ui.SetTestbtn.clicked.connect(src.app.load_tests.LoadTests.load_tests)
    mw.ui.NewTestbtn.clicked.connect(src.app.add_tests.AddTest.open_add_test)
    mw.ui.RunTestbtn.clicked.connect(src.app.open_tests.OpenTests.open_tests)
    mw.ui.AddSequencebtn.clicked.connect(src.app.sequence_window.SequenceWindow.sequence_window)
    mw.ui.Generatebtn.clicked.connect(src.app.generate_window.OpenGen.open_gen)

    sys.exit(application.exec_())
