from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 432)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultArea = QWidget(Dialog)
        self.resultArea.setObjectName(u"resultArea")
        self.verticalLayout = QVBoxLayout(self.resultArea)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addWidget(self.resultArea)

        self.Resultslbl = QLabel(Dialog)
        self.Resultslbl.setObjectName(u"Resultslbl")
        self.Resultslbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Resultslbl)

        self.resultTable = QTableView(Dialog)
        self.resultTable.setObjectName(u"resultTable")

        self.verticalLayout_2.addWidget(self.resultTable)

        self.ButtonArea = QWidget(Dialog)
        self.ButtonArea.setObjectName(u"ButtonArea")
        self.horizontalLayout = QHBoxLayout(self.ButtonArea)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.ButtonArea)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.ButtonArea)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.ButtonArea)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.ButtonArea)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Resultslbl.setText(QCoreApplication.translate("Dialog", u"Results", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Summary", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Cancel", None))

