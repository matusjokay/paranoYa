import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.AddTestWindow import Ui_AddTestWindow
import app.main_window


class AddTest:
    def open_add_test(self):
        mw = app.main_window.MainWindow.getInstance()
        mw.window = QtWidgets.QDialog()
        mw.ui = Ui_AddTestWindow()
        mw.ui.setupUi(mw.window)
        mw.window.show()

#
# for filename in os.listdir("tests/NIST"):
#     if filename[0].isdigit():
#         item = QtWidgets.QListWidgetItem()
#         Ui_AddTestWindow.Test_List.addItem(item)
#
#
# item_count = 0
# for filename in os.listdir("tests/NIST"):
#     if filename[0].isdigit():
#         item = Ui_AddTestWindow.Test_List.item(item_count)
#         item.setText(filename[3:-3])
#         item_count += 1
