from PyQt5 import QtWidgets, QtCore, QtGui, uic
from os import getcwd,system

class VPad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vpadui.ui", self) 
        self.assignValues()

    def assignValues(self):
        self.Button_Run = self.findChild(QtWidgets.QPushButton, "Button_Run")
        self.Button_Run.clicked.connect(self.Run)
        self.Button_Clear = self.findChild(QtWidgets.QPushButton, "Button_Clear")
        self.Button_Clear.clicked.connect(self.Clear)
        self.Button_Clear_Console = self.findChild(QtWidgets.QPushButton, "Button_Clear_Console")
        self.Button_Clear_Console.clicked.connect(self.Clear_Console)
        self.plainTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "plainTextEdit")
        self.Font_Slider = self.findChild(QtWidgets.QAbstractSlider, "Font_Slider")
        self.Font_Slider.setValue(10)
        self.Font_Slider.valueChanged.connect(self.SetNewFontSize)
        self.actionClose = self.findChild(QtWidgets.QAction, "actionClose")
        self.actionClose.triggered.connect(QtWidgets.QApplication.instance().quit)
        self.actionSave = self.findChild(QtWidgets.QAction, "actionSave")
        self.actionOpen = self.findChild(QtWidgets.QAction, "actionOpen")
        self.actionSave_As = self.findChild(QtWidgets.QAction, "actionSave_As")
        self.actionVPad = self.findChild(QtWidgets.QAction, "actionVPad")
        self.actionVedik_Cyber_Forces = self.findChild(QtWidgets.QAction, "actionVedik_Cyber_Forces")
        self.actionVPad.triggered.connect(self.AboutVpad)
        self.actionVedik_Cyber_Forces.triggered.connect(self.AboutVCF)
        self.actionOpen.triggered.connect(self.Open)
        self.code = self.plainTextEdit.toPlainText()
        self.actionSave_As.triggered.connect(self.SaveAs)
        self.actionSave.triggered.connect(self.Save)
    def Open(self):
        #open file code here
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Open File',"C:/", "Python Files (*.py)")
        self.currentfilepath = filename[0]
        self.currentfile = open(self.currentfilepath, "r")
        self.code = self.currentfile.read()
        self.plainTextEdit.setPlainText(self.code)
        self.currentfile.close()

    def AboutVpad(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("VPad is a simple Python IDE created by VCF")
        msg.setInformativeText("License - GNU GPL v3.0")
        msg.setWindowTitle("About VPad")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def AboutVCF(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("For Information About Vedik Cyber Forces \n Go to https://vcfstudio.in")
        msg.setWindowTitle("About VCF")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def Clear(self):
        self.plainTextEdit.setPlainText("")
    
    def SaveAs(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save File','C:/',"Python Files (*.py)")
        self.currentfilepath = filename[0]
        self.currentfile = open(self.currentfilepath, "w")
        self.code = self.plainTextEdit.toPlainText()
        self.currentfile.write(self.code)
        self.currentfile.close()

    def Save(self):
        if(self.currentfilepath is not ""):
            self.currentfile = open(self.currentfilepath, "w")
            self.code = self.plainTextEdit.toPlainText()
            self.currentfile.write(self.code)
            self.currentfile.close()
        else: 
            pass

    def SetNewFontSize(self):
        newfont = QtGui.QFont()
        newfont.setPointSize(self.Font_Slider.value())
        self.plainTextEdit.setFont(newfont)

    def Run(self):
        self.currentfile = open("defaultindexfile.py", "w")
        self.code = self.plainTextEdit.toPlainText()
        self.currentfile.write(self.code)
        self.currentfile.close()
        self.runfile = getcwd() + "/" + self.currentfile.name
        system("python " + self.runfile)
    
    def Clear_Console(self):
        system("cls")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vpad = VPad()
    vpad.show()
    sys.exit(app.exec())