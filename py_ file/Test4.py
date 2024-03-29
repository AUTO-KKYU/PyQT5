import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test4.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Add.clicked.connect(self.addText)
        self.FontUbuntu.clicked.connect(lambda: self.setFont("Ubuntu"))
        self.FontNanumGothic.clicked.connect(lambda: self.setFont("NanumGothic"))
        
        self.Red.clicked.connect(lambda: self.setTextColor(255, 0, 0))
        self.Green.clicked.connect(lambda: self.setTextColor(0, 255, 0))
        self.Blue.clicked.connect(lambda: self.setTextColor(0, 0, 255))
       
        self.SetFontSize.clicked.connect(self.setTextSize)
        
        
    def addText(self):
        input = self.Input.toPlainText()
        self.Input.clear()
        self.Output.append(input)
        
    def setFont(self, fontName):
        font = QFont(fontName, 11)
        self.Output.setFont(font)
        
    def setTextColor(self, r, g, b):
        color = QColor(r, g, b)
        self.Output.selectAll()
        self.Output.setTextColor(color)
        self.Output.moveCursor(QTextCursor.End)
        
    def setTextSize(self):
        size = int(self.FontSize.text())
        self.Output.selectAll()
        self.Output.setFontPointSize(size)
        self.Output.moveCursor(QTextCursor.End)
        
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴