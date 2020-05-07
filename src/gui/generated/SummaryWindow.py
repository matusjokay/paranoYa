# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SummaryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SummaryWindow(object):
    def setupUi(self, SummaryWindow):
        SummaryWindow.setObjectName("SummaryWindow")
        SummaryWindow.resize(642, 448)
        self.verticalLayout = QtWidgets.QVBoxLayout(SummaryWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenamelbl = QtWidgets.QLabel(SummaryWindow)
        self.filenamelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.filenamelbl.setObjectName("filenamelbl")
        self.verticalLayout.addWidget(self.filenamelbl)
        self.Dialog = QtWidgets.QTableView(SummaryWindow)
        self.Dialog.setBaseSize(QtCore.QSize(3, 10))
        self.Dialog.setObjectName("Dialog")
        self.verticalLayout.addWidget(self.Dialog)

        self.retranslateUi(SummaryWindow)
        QtCore.QMetaObject.connectSlotsByName(SummaryWindow)

    def retranslateUi(self, SummaryWindow):
        _translate = QtCore.QCoreApplication.translate
        SummaryWindow.setWindowTitle(_translate("SummaryWindow", "Dialog"))
        self.filenamelbl.setText(_translate("SummaryWindow", "\"Filename\" summary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SummaryWindow = QtWidgets.QDialog()
    ui = Ui_SummaryWindow()
    ui.setupUi(SummaryWindow)
    SummaryWindow.show()
    sys.exit(app.exec_())
