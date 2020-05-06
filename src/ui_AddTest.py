from PySide2.QtCore import QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(692, 546)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.Info_Area = QWidget(Dialog)
        self.Info_Area.setObjectName(u"Info_Area")
        self.horizontalLayout = QHBoxLayout(self.Info_Area)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TestArea = QWidget(self.Info_Area)
        self.TestArea.setObjectName(u"TestArea")
        self.verticalLayout_3 = QVBoxLayout(self.TestArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Test_Combo = QComboBox(self.TestArea)
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.addItem("")
        self.Test_Combo.setObjectName(u"Test_Combo")

        self.verticalLayout_3.addWidget(self.Test_Combo)

        self.Test_List = QListWidget(self.TestArea)
        QListWidgetItem(self.Test_List)
        QListWidgetItem(self.Test_List)
        self.Test_List.setObjectName(u"Test_List")

        self.verticalLayout_3.addWidget(self.Test_List)


        self.horizontalLayout.addWidget(self.TestArea)

        self.InputArea = QWidget(self.Info_Area)
        self.InputArea.setObjectName(u"InputArea")
        self.verticalLayout_2 = QVBoxLayout(self.InputArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Param1_lbl = QLabel(self.InputArea)
        self.Param1_lbl.setObjectName(u"Param1_lbl")

        self.verticalLayout_2.addWidget(self.Param1_lbl)

        self.Param1_input = QLineEdit(self.InputArea)
        self.Param1_input.setObjectName(u"Param1_input")

        self.verticalLayout_2.addWidget(self.Param1_input)

        self.Param2_lbl = QLabel(self.InputArea)
        self.Param2_lbl.setObjectName(u"Param2_lbl")

        self.verticalLayout_2.addWidget(self.Param2_lbl)

        self.Param2_input = QLineEdit(self.InputArea)
        self.Param2_input.setObjectName(u"Param2_input")

        self.verticalLayout_2.addWidget(self.Param2_input)

        self.Param3_lbl = QLabel(self.InputArea)
        self.Param3_lbl.setObjectName(u"Param3_lbl")

        self.verticalLayout_2.addWidget(self.Param3_lbl)

        self.Param3_input = QLineEdit(self.InputArea)
        self.Param3_input.setObjectName(u"Param3_input")

        self.verticalLayout_2.addWidget(self.Param3_input)


        self.horizontalLayout.addWidget(self.InputArea)


        self.verticalLayout_4.addWidget(self.Info_Area)

        self.verticalSpacer_2 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 56, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.ButtonArea = QWidget(Dialog)
        self.ButtonArea.setObjectName(u"ButtonArea")
        self.verticalLayout = QVBoxLayout(self.ButtonArea)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Savebtn = QPushButton(self.ButtonArea)
        self.Savebtn.setObjectName(u"Savebtn")

        self.verticalLayout.addWidget(self.Savebtn)

        self.Loadbtn = QPushButton(self.ButtonArea)
        self.Loadbtn.setObjectName(u"Loadbtn")

        self.verticalLayout.addWidget(self.Loadbtn)


        self.verticalLayout_4.addWidget(self.ButtonArea)

        self.horizontalSpacer = QSpacerItem(671, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Test_Combo.setItemText(0, QCoreApplication.translate("Dialog", u"Test1", None))
        self.Test_Combo.setItemText(1, QCoreApplication.translate("Dialog", u"Test2", None))
        self.Test_Combo.setItemText(2, QCoreApplication.translate("Dialog", u"Test3", None))
        self.Test_Combo.setItemText(3, QCoreApplication.translate("Dialog", u"Test4", None))


        __sortingEnabled = self.Test_List.isSortingEnabled()
        self.Test_List.setSortingEnabled(False)
        ___qlistwidgetitem = self.Test_List.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Test1", None));
        ___qlistwidgetitem1 = self.Test_List.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Test2", None));
        self.Test_List.setSortingEnabled(__sortingEnabled)

        self.Param1_lbl.setText(QCoreApplication.translate("Dialog", u"Param1", None))
        self.Param2_lbl.setText(QCoreApplication.translate("Dialog", u"Param2", None))
        self.Param3_lbl.setText(QCoreApplication.translate("Dialog", u"Param3", None))
        self.Savebtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Loadbtn.setText(QCoreApplication.translate("Dialog", u"Load", None))

