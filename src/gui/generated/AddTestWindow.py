# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTest.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTestWindow(object):
    def setupUi(self, AddTestWindow):
        AddTestWindow.setObjectName("AddTestWindow")
        AddTestWindow.resize(692, 546)
        AddTestWindow.setWindowOpacity(1.0)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(AddTestWindow)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.Info_Area = QtWidgets.QWidget(AddTestWindow)
        self.Info_Area.setObjectName("Info_Area")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Info_Area)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TestArea = QtWidgets.QWidget(self.Info_Area)
        self.TestArea.setObjectName("TestArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.TestArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Test_Combo = QtWidgets.QComboBox(self.TestArea)
        self.Test_Combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Test_Combo.setStyleSheet("")
        self.Test_Combo.setObjectName("Test_Combo")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.verticalLayout_3.addWidget(self.Test_Combo)
        self.widget = QtWidgets.QWidget(self.TestArea)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.RemoveAllbtn = QtWidgets.QPushButton(self.widget)
        self.RemoveAllbtn.setObjectName("RemoveAllbtn")
        self.gridLayout.addWidget(self.RemoveAllbtn, 1, 2, 1, 1)
        self.AddAllbtn = QtWidgets.QPushButton(self.widget)
        self.AddAllbtn.setObjectName("AddAllbtn")
        self.gridLayout.addWidget(self.AddAllbtn, 0, 2, 1, 1)
        self.Removebtn = QtWidgets.QPushButton(self.widget)
        self.Removebtn.setObjectName("Removebtn")
        self.gridLayout.addWidget(self.Removebtn, 1, 1, 1, 1)
        self.Addbtn = QtWidgets.QPushButton(self.widget)
        self.Addbtn.setStyleSheet("")
        self.Addbtn.setObjectName("Addbtn")
        self.gridLayout.addWidget(self.Addbtn, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget)
        self.Test_List = QtWidgets.QListWidget(self.TestArea)
        self.Test_List.setObjectName("Test_List")
        item = QtWidgets.QListWidgetItem()
        self.Test_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Test_List.addItem(item)
        self.verticalLayout_3.addWidget(self.Test_List)
        self.horizontalLayout.addWidget(self.TestArea)
        self.InputArea = QtWidgets.QWidget(self.Info_Area)
        self.InputArea.setObjectName("InputArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InputArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Param1_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param1_lbl.setObjectName("Param1_lbl")
        self.verticalLayout_2.addWidget(self.Param1_lbl)
        self.Param1_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param1_input.setObjectName("Param1_input")
        self.verticalLayout_2.addWidget(self.Param1_input)
        self.Param2_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param2_lbl.setObjectName("Param2_lbl")
        self.verticalLayout_2.addWidget(self.Param2_lbl)
        self.Param2_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param2_input.setObjectName("Param2_input")
        self.verticalLayout_2.addWidget(self.Param2_input)
        self.Param3_lbl = QtWidgets.QLabel(self.InputArea)
        self.Param3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Param3_lbl.setObjectName("Param3_lbl")
        self.verticalLayout_2.addWidget(self.Param3_lbl)
        self.Param3_input = QtWidgets.QLineEdit(self.InputArea)
        self.Param3_input.setObjectName("Param3_input")
        self.verticalLayout_2.addWidget(self.Param3_input)
        self.Setbtn = QtWidgets.QPushButton(self.InputArea)
        self.Setbtn.setObjectName("Setbtn")
        self.verticalLayout_2.addWidget(self.Setbtn)
        self.horizontalLayout.addWidget(self.InputArea)
        self.verticalLayout_4.addWidget(self.Info_Area)
        spacerItem2 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.ButtonArea = QtWidgets.QWidget(AddTestWindow)
        self.ButtonArea.setObjectName("ButtonArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ButtonArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Savebtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Savebtn.setObjectName("Savebtn")
        self.verticalLayout.addWidget(self.Savebtn)
        self.Loadbtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Loadbtn.setObjectName("Loadbtn")
        self.verticalLayout.addWidget(self.Loadbtn)
        self.verticalLayout_4.addWidget(self.ButtonArea)
        spacerItem4 = QtWidgets.QSpacerItem(671, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)

        self.retranslateUi(AddTestWindow)
        QtCore.QMetaObject.connectSlotsByName(AddTestWindow)

    def retranslateUi(self, AddTestWindow):
        _translate = QtCore.QCoreApplication.translate
        AddTestWindow.setWindowTitle(_translate("AddTestWindow", "Add Test"))
        self.Test_Combo.setItemText(0, _translate("AddTestWindow", "Test1"))
        self.Test_Combo.setItemText(1, _translate("AddTestWindow", "Test2"))
        self.Test_Combo.setItemText(2, _translate("AddTestWindow", "Test3"))
        self.Test_Combo.setItemText(3, _translate("AddTestWindow", "Test4"))
        self.RemoveAllbtn.setText(_translate("AddTestWindow", "Remove  All"))
        self.AddAllbtn.setText(_translate("AddTestWindow", "Add All"))
        self.Removebtn.setText(_translate("AddTestWindow", "Remove"))
        self.Addbtn.setText(_translate("AddTestWindow", "Add"))
        __sortingEnabled = self.Test_List.isSortingEnabled()
        self.Test_List.setSortingEnabled(False)
        item = self.Test_List.item(0)
        item.setText(_translate("AddTestWindow", "Test1"))
        item = self.Test_List.item(1)
        item.setText(_translate("AddTestWindow", "Test2"))
        self.Test_List.setSortingEnabled(__sortingEnabled)
        self.Param1_lbl.setText(_translate("AddTestWindow", "Param1"))
        self.Param1_input.setText(_translate("AddTestWindow", "0.01"))
        self.Param2_lbl.setText(_translate("AddTestWindow", "Param2"))
        self.Param2_input.setText(_translate("AddTestWindow", "0.02"))
        self.Param3_lbl.setText(_translate("AddTestWindow", "Param3"))
        self.Param3_input.setText(_translate("AddTestWindow", "8848"))
        self.Setbtn.setText(_translate("AddTestWindow", "Set"))
        self.Savebtn.setText(_translate("AddTestWindow", "Save"))
        self.Loadbtn.setText(_translate("AddTestWindow", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTestWindow = QtWidgets.QDialog()
    ui = Ui_AddTestWindow()
    ui.setupUi(AddTestWindow)
    AddTestWindow.show()
    sys.exit(app.exec_())
