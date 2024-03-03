import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test3.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.clearText)
        self.pushButton.clicked.connect(self.addText)
        # Enter 키를 누르면 추가가 되도록 설정 
        self.lineEdit.returnPressed.connect(self.addText)
        
    def addText(self):
        input = self.lineEdit.text()
        self.lineEdit.clear()
        self.textBrowser.append(input)
        
    def clearText(self):
        self.lineEdit.clear()
        self.textBrowser.clear()
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴