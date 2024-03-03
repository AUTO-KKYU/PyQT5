import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test7.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnAdd.clicked.connect(self.Add)
        
    
    def Add(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(self.editName.text()))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(self.editGender.text()))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(self.editBirthday.text()))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴