# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from gui.generated.SummaryWindow import Ui_SummaryWindow


class Ui_ResultsWindow(object):


    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("Dialog")
        ResultsWindow.resize(610, 432)
        ResultsWindow.setStyleSheet("background-color:#D8D8D8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ResultsWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultArea = QtWidgets.QWidget(ResultsWindow)
        self.resultArea.setObjectName("resultArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.resultArea)
        self.Resultslbl = QtWidgets.QLabel(ResultsWindow)
        self.Resultslbl.setStyleSheet("color:#520202")
        self.Resultslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultslbl.setObjectName("Resultslbl")
        self.verticalLayout_2.addWidget(self.Resultslbl)
        self.resultTable = QtWidgets.QTableView(ResultsWindow)
        self.resultTable.setStyleSheet("background-color:#FFFFFF;color:#520202")
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout_2.addWidget(self.resultTable)
        self.ButtonArea = QtWidgets.QWidget(ResultsWindow)
        self.ButtonArea.setObjectName("ButtonArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_2.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.ButtonArea)
        self.pushButton_3.setStyleSheet("background-color:#790E0E;color:#F86262")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.ButtonArea)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("Dialog", "Results"))
        self.Resultslbl.setText(_translate("Dialog", "Results"))
        self.pushButton.setText(_translate("Dialog", "Summary"))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QDialog()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())
