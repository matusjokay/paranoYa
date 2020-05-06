from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 339)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Input_Area_Sequence = QWidget(Dialog)
        self.Input_Area_Sequence.setObjectName(u"Input_Area_Sequence")
        self.verticalLayout = QVBoxLayout(self.Input_Area_Sequence)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Input_path_lbl = QLabel(self.Input_Area_Sequence)
        self.Input_path_lbl.setObjectName(u"Input_path_lbl")

        self.verticalLayout.addWidget(self.Input_path_lbl)

        self.Path_Input = QLineEdit(self.Input_Area_Sequence)
        self.Path_Input.setObjectName(u"Path_Input")

        self.verticalLayout.addWidget(self.Path_Input)

        self.radbtn_1mb = QRadioButton(self.Input_Area_Sequence)
        self.radbtn_1mb.setObjectName(u"radbtn_1mb")

        self.verticalLayout.addWidget(self.radbtn_1mb)

        self.radbtn_10mb = QRadioButton(self.Input_Area_Sequence)
        self.radbtn_10mb.setObjectName(u"radbtn_10mb")

        self.verticalLayout.addWidget(self.radbtn_10mb)

        self.FileList = QListWidget(self.Input_Area_Sequence)
        self.FileList.setObjectName(u"FileList")

        self.verticalLayout.addWidget(self.FileList)

        self.horizontalLayout.addWidget(self.Input_Area_Sequence)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Input_path_lbl.setText(QCoreApplication.translate("Dialog", u"Set input path:", None))
        self.radbtn_1mb.setText(QCoreApplication.translate("Dialog", u"1 MB files", None))
        self.radbtn_10mb.setText(QCoreApplication.translate("Dialog", u"10 MB files", None))
