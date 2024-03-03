import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
import urllib.request 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/paint.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)
        
        self.label.setPixmap(self.pixmap)
        self.draw()
        
    def draw(self):
        painter = QPainter(self.label.pixmap())
        
        # 빨간색 solid line
        self.pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(self.pen)
        painter.drawLine(100, 100, 500, 100)
        
        # 파란색 dashdot line
        self.pen.setBrush(Qt.blue)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.DashDotLine)
        painter.setPen(self.pen)
        self.line = QLine(100, 200, 500, 200)
        painter.drawLine(self.line)
        
        # 검정색 dot line
        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))
        self.p1 = QPoint(100, 300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)
        
        # 빨간색 점 찍기
        painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        painter.drawPoint(100, 400)
        
        # 전체 검은색 사각형 그리기
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.drawRect(50 , 50, 500, 500)
        
        # 빨간색 사각형 내부에 검은색 칠하기
        painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.black))
        painter.drawRect(200,400, 100, 100)
        
        # 파란색 원 내부에 검은색 칠하기
        painter.setPen(QPen(Qt.blue, 10, Qt.DotLine))
        # painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(400,400, 100, 100)
        
        # ------------------------------ #
        
        # 전체 검은색 사각형 그리기
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.drawRect(600 , 50, 400, 500)
        
        # Text 그리기
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
        
        self.font = QFont()
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)
        painter.drawText(620, 90, 'This is drawText.')
        
        
        painter.end


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴