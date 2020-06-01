# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_TestingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestingWindow(object):
    def setupUi(self, TestingWindow):
        TestingWindow.setObjectName("TestingWindow")
        TestingWindow.resize(665, 519)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TestingWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(TestingWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pausebtn = QtWidgets.QPushButton(self.widget)
        self.Pausebtn.setObjectName("Pausebtn")
        self.verticalLayout_4.addWidget(self.Pausebtn)
        self.Continuebtn = QtWidgets.QPushButton(self.widget)
        self.Continuebtn.setObjectName("Continuebtn")
        self.verticalLayout_4.addWidget(self.Continuebtn)
        self.Cancelbtn = QtWidgets.QPushButton(self.widget)
        self.Cancelbtn.setObjectName("Cancelbtn")
        self.verticalLayout_4.addWidget(self.Cancelbtn)
        self.CancelAllbtn = QtWidgets.QPushButton(self.widget)
        self.CancelAllbtn.setObjectName("CancelAllbtn")
        self.verticalLayout_4.addWidget(self.CancelAllbtn)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(TestingWindow)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Info_Area = QtWidgets.QWidget(self.widget_2)
        self.Info_Area.setObjectName("Info_Area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info_Area)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Info_Text = QtWidgets.QWidget(self.Info_Area)
        self.Info_Text.setStyleSheet("")
        self.Info_Text.setObjectName("Info_Text")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Info_Text)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.Info_Text)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.Info_Text)
        self.textEdit = QtWidgets.QTextEdit(self.Info_Area)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3.addWidget(self.Info_Area)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(TestingWindow)
        QtCore.QMetaObject.connectSlotsByName(TestingWindow)

    def retranslateUi(self, TestingWindow):
        _translate = QtCore.QCoreApplication.translate
        TestingWindow.setWindowTitle(_translate("TestingWindow", "Testing"))
        self.Pausebtn.setText(_translate("TestingWindow", "Pause"))
        self.Continuebtn.setText(_translate("TestingWindow", "Continue"))
        self.Cancelbtn.setText(_translate("TestingWindow", "Cancel"))
        self.CancelAllbtn.setText(_translate("TestingWindow", "CancelAll"))
        self.label.setText(_translate("TestingWindow", "Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestingWindow = QtWidgets.QDialog()
    ui = Ui_TestingWindow()
    ui.setupUi(TestingWindow)
    TestingWindow.show()
    sys.exit(app.exec_())
