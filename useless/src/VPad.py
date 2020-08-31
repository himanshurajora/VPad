from PyQt5 import QtWidgets, QtCore, QtGui, uic
from os import getcwd
import os


class VPad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.SetupUi()      
        self.file_saved = False

    def SetupUi(self):
        self.setWindowTitle("hello")
        self.setGeometry(0,0,1350,950)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.Button_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Clear.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Button_Clear.setFont(font)
        self.Button_Clear.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Button_Clear.setMouseTracking(False)
        self.Button_Clear.setObjectName("Button_Clear")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Button_Clear)
        self.Button_Run = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Button_Run.setFont(font)
        self.Button_Run.setObjectName("Button_Run")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Button_Run)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionVPad = QtWidgets.QAction(self)
        self.actionVPad.setObjectName("actionVPad")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionVPad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.actionClose.setShortcut("Ctrl + Q")
        self.actionClose.triggered.connect(self.Close)
        self.Button_Run.clicked.connect(self.Run)
        self.Button_Clear.clicked.connect(self.Clear)
        self.show()
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "VPad"))
        self.Button_Clear.setText(_translate("MainWindow", "Clear"))
        self.Button_Run.setText(_translate("MainWindow", "Run"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionVPad.setText(_translate("MainWindow", "VPad"))
    def Close(self):
        QtWidgets.QApplication.quit()

    def Clear(self):
        self.plainTextEdit.setPlainText("")
    # def Save(self):
    #     self.code = self.plainTextEdit.toPlainText()
    #     self.filename = self.currentfile.name
    #     self.currentfile = open(self.filename, "w")
    #     self.currentfile.writelines(self.code)
    #     self.currentfile.close()
    def Run(self):
        self.currentfile = open("defaultindexfile.py", "w")
        self.code = self.plainTextEdit.toPlainText()
        self.currentfile.write(self.code)
        self.currentfile.close()
        self.runfile = getcwd() + "/" + self.currentfile.name
        os.system("python " + self.runfile)
        

    def SaveAs(self):
        self.filename, ok = QtWidgets.QInputDialog.getText(self, "Save", "Enter file name to save as: ")
        if ok:
            if self.filename == "":
                self.filename = "index.py"
                self.currentfile = open(self.filename, "w")
                self.Save()
            else:
                self.currentfile = open(self.filename + ".py", "w")
                self.file_saved = True
                self.Save()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vpad = VPad()
    vpad.show()
    sys.exit(app.exec())