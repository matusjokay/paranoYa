import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.AddTestWindow import Ui_AddTestWindow
import src.app.main_window


class AddTest:
    def open_add_test(self):
        mw = src.app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_AddTestWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()

        mw.test_sets = list()

        for filename in os.listdir("src/tests/NIST"):
            if filename[0].isdigit():
                item = QtWidgets.QListWidgetItem()
                mw.ui.Test_List.addItem(item)


        item_count = 0
        for filename in os.listdir("src/tests/NIST"):
            if filename[0].isdigit():
                item = mw.ui.Test_List.item(item_count)
                item.setText(filename[3:-3])
                item_count += 1


        mw.test_sets.push([1,2,3,4,5,6,7])
        mw.loaded_test_set = [1, 2, 3, 4, 5, 6, 7]