# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailedResultsByFilename.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SummaryWindow(object):
    def setupUi(self, SummaryWindow):
        SummaryWindow.setObjectName("Dialog")
        SummaryWindow.resize(642, 448)
        SummaryWindow.setStyleSheet("background-color:#D8D8D8")
        self.verticalLayout = QtWidgets.QVBoxLayout(SummaryWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenamelbl = QtWidgets.QLabel(SummaryWindow)
        self.filenamelbl.setStyleSheet("color:#520202")
        self.filenamelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.filenamelbl.setObjectName("filenamelbl")
        self.verticalLayout.addWidget(self.filenamelbl)
        self.Detailedresultstable = QtWidgets.QTableView(SummaryWindow)
        self.Detailedresultstable.setBaseSize(QtCore.QSize(3, 10))
        self.Detailedresultstable.setStyleSheet("background-color:#FFFFFF")
        self.Detailedresultstable.setObjectName("Detailedresultstable")
        self.verticalLayout.addWidget(self.Detailedresultstable)

        self.retranslateUi(SummaryWindow)
        QtCore.QMetaObject.connectSlotsByName(SummaryWindow)

    def retranslateUi(self, SummaryWindow):
        _translate = QtCore.QCoreApplication.translate
        SummaryWindow.setWindowTitle(_translate("Dialog", "\"Filename\" summary"))
        self.filenamelbl.setText(_translate("Dialog", "\"Filename\" summary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SummaryWindow = QtWidgets.QDialog()
    ui = Ui_SummaryWindow()
    ui.setupUi(SummaryWindow)
    SummaryWindow.show()
    sys.exit(app.exec_())
