# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Generate_SubWindowiPNRuf.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Generate(object):
    def setupUi(self, Generate):
        if Generate.objectName():
            Generate.setObjectName(u"Generate")
        Generate.resize(268, 248)
        self.verticalLayout_3 = QVBoxLayout(Generate)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ButtonBox = QWidget(Generate)
        self.ButtonBox.setObjectName(u"ButtonBox")
        self.verticalLayout = QVBoxLayout(self.ButtonBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GenInfobtn = QPushButton(self.ButtonBox)
        self.GenInfobtn.setObjectName(u"GenInfobtn")

        self.verticalLayout.addWidget(self.GenInfobtn)

        self.GenGeneratebtn = QPushButton(self.ButtonBox)
        self.GenGeneratebtn.setObjectName(u"GenGeneratebtn")

        self.verticalLayout.addWidget(self.GenGeneratebtn)


        self.verticalLayout_3.addWidget(self.ButtonBox)

        self.ParamBox = QWidget(Generate)
        self.ParamBox.setObjectName(u"ParamBox")
        self.verticalLayout_2 = QVBoxLayout(self.ParamBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GenParam1lbl = QLabel(self.ParamBox)
        self.GenParam1lbl.setObjectName(u"GenParam1lbl")

        self.verticalLayout_2.addWidget(self.GenParam1lbl)

        self.GenInput1 = QLineEdit(self.ParamBox)
        self.GenInput1.setObjectName(u"GenInput1")

        self.verticalLayout_2.addWidget(self.GenInput1)

        self.GenParam2lbl = QLabel(self.ParamBox)
        self.GenParam2lbl.setObjectName(u"GenParam2lbl")

        self.verticalLayout_2.addWidget(self.GenParam2lbl)

        self.GenInput2 = QLineEdit(self.ParamBox)
        self.GenInput2.setObjectName(u"GenInput2")

        self.verticalLayout_2.addWidget(self.GenInput2)

        self.GenParam3lbl = QLabel(self.ParamBox)
        self.GenParam3lbl.setObjectName(u"GenParam3lbl")

        self.verticalLayout_2.addWidget(self.GenParam3lbl)

        self.GenInput3 = QLineEdit(self.ParamBox)
        self.GenInput3.setObjectName(u"GenInput3")

        self.verticalLayout_2.addWidget(self.GenInput3)


        self.verticalLayout_3.addWidget(self.ParamBox)


        self.retranslateUi(Generate)

        QMetaObject.connectSlotsByName(Generate)


    def retranslateUi(self, Generate):
        Generate.setWindowTitle(QCoreApplication.translate("Generate", u"Dialog", None))
        self.GenInfobtn.setText(QCoreApplication.translate("Generate", u"Info", None))
        self.GenGeneratebtn.setText(QCoreApplication.translate("Generate", u"Generate", None))
        self.GenParam1lbl.setText(QCoreApplication.translate("Generate", u"Parameter1", None))
        self.GenParam2lbl.setText(QCoreApplication.translate("Generate", u"Parameter2", None))
        self.GenParam3lbl.setText(QCoreApplication.translate("Generate", u"Parameter3", None))

