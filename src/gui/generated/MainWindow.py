# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from src.gui.generated.AddTestWindow import Ui_AddTestWindow
from src.gui.generated.GenerateWindow import Ui_GenerateWindow
from src.gui.generated.LoadTestWindow import Ui_LoadTestWindow
from src.gui.generated.ResultsWindow import Ui_ResultsWindow
from src.gui.generated.SequenceWindow import Ui_SequenceWindow
from src.gui.generated.SummaryWindow import Ui_SummaryWindow
from src.gui.generated.TestingWindow import Ui_TestingWindow

class Ui_MainWindow(object):

     def openGen(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_GenerateWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAddTest(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AddTestWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRes(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ResultsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSeq(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SequenceWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSum(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SummaryWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openTest(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_TestingWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLoad(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_LoadTestWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.NewTestbtn = QtWidgets.QPushButton(self.widget)
        self.NewTestbtn.setObjectName("NewTestbtn")
        self.verticalLayout.addWidget(self.NewTestbtn)
        self.AddSequencebtn = QtWidgets.QPushButton(self.widget)
        self.AddSequencebtn.setObjectName("AddSequencebtn")
        self.verticalLayout.addWidget(self.AddSequencebtn)
        self.Generatebtn = QtWidgets.QPushButton(self.widget)
        self.Generatebtn.setObjectName("Generatebtn")
        self.verticalLayout.addWidget(self.Generatebtn)
        self.RunTestbtn = QtWidgets.QPushButton(self.widget)
        self.RunTestbtn.setObjectName("RunTestbtn")
        self.verticalLayout.addWidget(self.RunTestbtn)
        self.SetTestbtn = QtWidgets.QPushButton(self.widget)
        self.SetTestbtn.setObjectName("SetTestbtn")
        self.verticalLayout.addWidget(self.SetTestbtn)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.widget)
        self.Info_Area = QtWidgets.QWidget(self.centralwidget)
        self.Info_Area.setObjectName("Info_Area")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Info_Area)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Info_Text = QtWidgets.QWidget(self.Info_Area)
        self.Info_Text.setObjectName("Info_Text")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Info_Text)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.Info_Text)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.Info_Text)
        self.textEdit = QtWidgets.QTextEdit(self.Info_Area)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.Info_Area)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOption.addAction(self.actionUndo)
        self.menuOption.addAction(self.actionRedo)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionCut)
        self.menuOption.addAction(self.actionPaste)
        self.menuOption.addAction(self.actionCopy)
        self.menuOption.addAction(self.actionDelete)
        self.menuHelp.addAction(self.actionManual)
        self.menuAbout.addAction(self.actionCredits)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

	self.Generatebtn.clicked.connect(self.openGen)
        self.SetTestbtn.clicked.connect(self.openLoad)
        self.NewTestbtn.clicked.connect(self.openAddTest)
        self.RunTestbtn.clicked.connect(self.openTest)
        self.AddSequencebtn.clicked.connect(self.openSeq)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ParanoYa"))
        self.NewTestbtn.setText(_translate("MainWindow", "New Test"))
        self.AddSequencebtn.setText(_translate("MainWindow", "Add sequence"))
        self.Generatebtn.setText(_translate("MainWindow", "Generate"))
        self.RunTestbtn.setText(_translate("MainWindow", "Run Test"))
        self.SetTestbtn.setText(_translate("MainWindow", "Set test"))
        self.label.setText(_translate("MainWindow", "Information"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
