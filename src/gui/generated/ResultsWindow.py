# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ResultsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from src.gui.generated.SummaryWindow import Ui_SummaryWindow


class Ui_ResultsWindow(object):


    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(610, 432)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ResultsWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultArea = QtWidgets.QWidget(ResultsWindow)
        self.resultArea.setObjectName("resultArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.resultArea)
        self.Resultslbl = QtWidgets.QLabel(ResultsWindow)
        self.Resultslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultslbl.setObjectName("Resultslbl")
        self.verticalLayout_2.addWidget(self.Resultslbl)
        self.resultTable = QtWidgets.QTableView(ResultsWindow)
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout_2.addWidget(self.resultTable)
        self.ButtonArea = QtWidgets.QWidget(ResultsWindow)
        self.ButtonArea.setObjectName("ButtonArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Summarybtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Summarybtn.setObjectName("Summarybtn")
        self.horizontalLayout.addWidget(self.Summarybtn)
        self.Okbtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Okbtn.setObjectName("Okbtn")
        self.horizontalLayout.addWidget(self.Okbtn)
        self.Cancelbtn = QtWidgets.QPushButton(self.ButtonArea)
        self.Cancelbtn.setObjectName("Cancelbtn")
        self.horizontalLayout.addWidget(self.Cancelbtn)
        self.verticalLayout_2.addWidget(self.ButtonArea)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "Results"))
        self.Resultslbl.setText(_translate("ResultsWindow", "Results"))
        self.Summarybtn.setText(_translate("ResultsWindow", "Summary"))
        self.Okbtn.setText(_translate("ResultsWindow", "Ok"))
        self.Cancelbtn.setText(_translate("ResultsWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QDialog()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()
    sys.exit(app.exec_())
