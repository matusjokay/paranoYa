# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(610, 432)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ResultWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultArea = QtWidgets.QWidget(ResultWindow)
        self.resultArea.setObjectName("resultArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.resultArea)
        self.Resultslbl = QtWidgets.QLabel(ResultWindow)
        self.Resultslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultslbl.setObjectName("Resultslbl")
        self.verticalLayout_2.addWidget(self.Resultslbl)
        self.resultTable = QtWidgets.QTableView(ResultWindow)
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout_2.addWidget(self.resultTable)
        self.ButtonArea = QtWidgets.QWidget(ResultWindow)
        self.ButtonArea.setObjectName("ButtonArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.ButtonArea)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Dialog"))
        self.Resultslbl.setText(_translate("ResultWindow", "Results"))
        self.pushButton.setText(_translate("ResultWindow", "Summary"))
        self.pushButton_2.setText(_translate("ResultWindow", "Ok"))
        self.pushButton_3.setText(_translate("ResultWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultWindow = QtWidgets.QDialog()
    ui = Ui_ResultWindow()
    ui.setupUi(ResultWindow)
    ResultWindow.show()
    sys.exit(app.exec_())
