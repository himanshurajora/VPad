
from PyQt5 import QtCore, QtGui, QtWidgets
from os import system, getcwd

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_Run = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_Run.setFont(font)
        self.Button_Run.setObjectName("Button_Run")
        self.verticalLayout.addWidget(self.Button_Run, 0, QtCore.Qt.AlignLeft)
        self.Button_Clear_Console = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_Clear_Console.setFont(font)
        self.Button_Clear_Console.setObjectName("Button_Clear_Console")
        self.verticalLayout.addWidget(self.Button_Clear_Console)
        self.Button_Clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_Clear.setFont(font)
        self.Button_Clear.setObjectName("Button_Clear")
        self.verticalLayout.addWidget(self.Button_Clear, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Font_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Font_Slider.setMinimum(7)
        self.Font_Slider.setMaximum(72)
        self.Font_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Font_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Font_Slider.setObjectName("Font_Slider")
        self.verticalLayout_2.addWidget(self.Font_Slider, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuVPad = QtWidgets.QMenu(self.menubar)
        self.menuVPad.setObjectName("menuVPad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionVPad = QtWidgets.QAction(MainWindow)
        self.actionVPad.setObjectName("actionVPad")
        self.actionVedik_Cyber_Forces = QtWidgets.QAction(MainWindow)
        self.actionVedik_Cyber_Forces.setObjectName("actionVedik_Cyber_Forces")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuVPad.addAction(self.actionVPad)
        self.menuVPad.addSeparator()
        self.menuVPad.addAction(self.actionVedik_Cyber_Forces)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVPad.menuAction())
        self.Button_Run.clicked.connect(self.Run)
        self.Button_Clear.clicked.connect(self.Clear)
        self.Button_Clear_Console.clicked.connect(self.Clear_Console)
        self.Font_Slider.valueChanged.connect(self.SetNewFontSize)
        self.actionClose.triggered.connect(QtWidgets.QApplication.instance().quit)
        self.actionVPad.triggered.connect(self.AboutVpad)
        self.actionVedik_Cyber_Forces.triggered.connect(self.AboutVCF)
        self.actionOpen.triggered.connect(self.Open)
        self.code = self.plainTextEdit.toPlainText()
        self.actionSave_As.triggered.connect(self.SaveAs)
        self.actionSave.triggered.connect(self.Save)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VPad"))
        self.Button_Run.setText(_translate("MainWindow", "Run"))
        self.Button_Clear_Console.setText(_translate("MainWindow", "Clear Console"))
        self.Button_Clear.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Font Size"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuVPad.setTitle(_translate("MainWindow", "VPad"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionVPad.setText(_translate("MainWindow", "VPad"))
        self.actionVedik_Cyber_Forces.setText(_translate("MainWindow", "Vedik Cyber Forces"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        
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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())