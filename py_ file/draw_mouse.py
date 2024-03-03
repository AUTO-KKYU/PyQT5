import sys
from PyQt5.QtGui import QMouseEvent
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
import urllib.request 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/draw_mouse.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)
        
        self.label.setPixmap(self.pixmap)
        self.x, self.y = None, None
        
    def mouseMoveEvent(self, event):
        if self.x is None:
            self.x = event.x()
            self.y = event.y()
            return
        
        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.x, self.y, event.x(), event.y())
        painter.end()
        self.update()
        
        self.x = event.x()
        self.y = event.y()
        
    def mouseReleaseEvent(self, event):
        self.x = None
        self.y = None

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴