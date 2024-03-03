import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5 import uic
from PyQt5.QtCore import * 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test6.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for year in range(1900, 2022 + 1):
            self.cbYear.addItem(str(year))
            
        for month in range(1, 12 + 1):
            self.cbMonth.addItem(str(month))
            
        for day in range(1, 31 + 1):
            self.cbDay.addItem(str(day))
            
        self.cbYear.setCurrentText(str(2000))
        self.cbMonth.setCurrentText(str(4))
        self.cbDay.setCurrentText(str(11))

        self.cbYear.currentIndexChanged.connect(self.printBirthday)
        self.cbMonth.currentIndexChanged.connect(self.printBirthday)        
        self.cbDay.currentIndexChanged.connect(self.printBirthday)

        self.calendarWidget.clicked.connect(self.selectDate)

        
    def printBirthday(self):
        year = self.cbYear.currentText()
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))
        
        current_date = QDate(int(year), int(month), int(day))
        self.calendarWidget.setSelectedDate(current_date)
        
    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')
        
        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)
        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴