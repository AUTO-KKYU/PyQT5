import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("Test.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("test PyQt!")
        
        # pushButton을 클릭하면 함수를 호출
        self.pushButton_1.clicked.connect(self.button1Clicked)
        self.pushButton_2.clicked.connect(self.button2Clicked)
        
        self.radio_1.clicked.connect(self.radioClicked)
        self.radio_2.clicked.connect(self.radioClicked)
        self.radio_3.clicked.connect(self.radioClicked)
        
        self.radio_4.clicked.connect(self.button4Clicked)
        self.radio_5.clicked.connect(self.button5Clicked)
        self.radio_6.clicked.connect(self.button6Clicked)
        
        self.checkBox_1.clicked.connect(self.check1_Clicked)
        self.checkBox_2.clicked.connect(self.check2_Clicked)
        self.checkBox_3.clicked.connect(self.check3_Clicked)
        self.checkBox_4.clicked.connect(self.check4_Clicked)
        
        
        
        # pushButton1 클릭 -> "Button 1" 출력
        # pushButton2 클릭 -> "Button 2" 출력
        
    def radioClicked(self):
        if self.radio_1.isChecked():
            self.textEdit2.setText("Radio 1")
        elif self.radio_2.isChecked():
            self.textEdit2.setText("Radio 2")
        elif self.radio_3.isChecked():
            self.textEdit2.setText("Radio 3")
        else:
            self.textEdit.setText("Unknown")
            
    def button1Clicked(self):
        self.textEdit.setText("Button 1")
        
    def button2Clicked(self):
        self.textEdit.setText("Button 2")
        
    def button4Clicked(self):
        self.textEdit3.setText("Button 1")
        self.radio_4.setChecked(True)

    def button5Clicked(self):
        self.textEdit3.setText("Button 2")
        self.radio_5.setChecked(True)   

    def button6Clicked(self):
        self.textEdit3.setText("Button 1")
        self.radio_6.setChecked(True)
        
        
    def check1_Clicked(self):
        if (self.checkBox_1.isChecked()):
            self.textEdit4.setText("CheckBox 1 checked")
            self.checkBox_5.setChecked(True)
        else:
            self.textEdit4.setText("CheckBox 1 unchecked")
            self.checkBox_5.setChecked(False)
            
        self.checkBox_5.setEnabled(False)

        
    def check2_Clicked(self):
        if (self.checkBox_2.isChecked()):
            self.textEdit4.setText("CheckBox 2 checked")
            self.checkBox_6.setChecked(True)
        else:
            self.textEdit4.setText("CheckBox 2 unchecked")
            self.checkBox_6.setChecked(False)
            
        self.checkBox_6.setEnabled(False)

    
    def check3_Clicked(self):
        if (self.checkBox_3.isChecked()):
            self.textEdit4.setText("CheckBox 3 checked")
            self.checkBox_7.setChecked(True)    
        else:
            self.textEdit4.setText("CheckBox 3 unchecked")
            self.checkBox_7.setChecked(False)
        
        self.checkBox_7.setEnabled(False)

    
    def check4_Clicked(self):
        if (self.checkBox_4.isChecked()):
            self.textEdit4.setText("CheckBox 4 checked")
            self.checkBox_8.setChecked(True)      
        else:
            self.textEdit4.setText("checkBox 4 unchecked")
            self.checkBox_8.setChecked(False)
        
        self.checkBox_8.setEnabled(False)

                      
    
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴