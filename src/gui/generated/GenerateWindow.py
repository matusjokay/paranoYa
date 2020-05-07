# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GenerateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GenerateWindow(object):
    def setupUi(self, GenerateWindow):
        GenerateWindow.setObjectName("GenerateWindow")
        GenerateWindow.resize(268, 285)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(GenerateWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ButtonBox = QtWidgets.QWidget(GenerateWindow)
        self.ButtonBox.setObjectName("ButtonBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ButtonBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GenInfobtn = QtWidgets.QPushButton(self.ButtonBox)
        self.GenInfobtn.setObjectName("GenInfobtn")
        self.verticalLayout.addWidget(self.GenInfobtn)
        self.GenGeneratebtn = QtWidgets.QPushButton(self.ButtonBox)
        self.GenGeneratebtn.setObjectName("GenGeneratebtn")
        self.verticalLayout.addWidget(self.GenGeneratebtn)
        self.verticalLayout_3.addWidget(self.ButtonBox)
        self.ParamBox = QtWidgets.QWidget(GenerateWindow)
        self.ParamBox.setObjectName("ParamBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ParamBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GenParam1lbl = QtWidgets.QLabel(self.ParamBox)
        self.GenParam1lbl.setObjectName("GenParam1lbl")
        self.verticalLayout_2.addWidget(self.GenParam1lbl)
        self.GenInput1 = QtWidgets.QLineEdit(self.ParamBox)
        self.GenInput1.setObjectName("GenInput1")
        self.verticalLayout_2.addWidget(self.GenInput1)
        self.GenParam2lbl = QtWidgets.QLabel(self.ParamBox)
        self.GenParam2lbl.setObjectName("GenParam2lbl")
        self.verticalLayout_2.addWidget(self.GenParam2lbl)
        self.GenInput2 = QtWidgets.QLineEdit(self.ParamBox)
        self.GenInput2.setObjectName("GenInput2")
        self.verticalLayout_2.addWidget(self.GenInput2)
        self.GenParam3lbl = QtWidgets.QLabel(self.ParamBox)
        self.GenParam3lbl.setObjectName("GenParam3lbl")
        self.verticalLayout_2.addWidget(self.GenParam3lbl)
        self.GenInput3 = QtWidgets.QLineEdit(self.ParamBox)
        self.GenInput3.setObjectName("GenInput3")
        self.verticalLayout_2.addWidget(self.GenInput3)
        self.verticalLayout_3.addWidget(self.ParamBox)

        self.retranslateUi(GenerateWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerateWindow)

    def retranslateUi(self, GenerateWindow):
        _translate = QtCore.QCoreApplication.translate
        GenerateWindow.setWindowTitle(_translate("GenerateWindow", "Dialog"))
        self.GenInfobtn.setText(_translate("GenerateWindow", "Info"))
        self.GenGeneratebtn.setText(_translate("GenerateWindow", "Generate"))
        self.GenParam1lbl.setText(_translate("GenerateWindow", "Parameter1"))
        self.GenParam2lbl.setText(_translate("GenerateWindow", "Parameter2"))
        self.GenParam3lbl.setText(_translate("GenerateWindow", "Parameter3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GenerateWindow = QtWidgets.QDialog()
    ui = Ui_GenerateWindow()
    ui.setupUi(GenerateWindow)
    GenerateWindow.show()
    sys.exit(app.exec_())
