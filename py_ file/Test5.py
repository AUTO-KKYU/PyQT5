import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test5.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnInput.clicked.connect(self.inputName)
        self.btnSeason.clicked.connect(self.inputSeason)
        self.btnColor.clicked.connect(self.inputColor)
        self.btnFont.clicked.connect(self.inputFont)
        self.btnFile.clicked.connect(self.openFile)
        self.lineEdit.returnPressed.connect(self.inputNumber)
        
        
    def inputName(self):
        text, ok = QInputDialog.getText(self, 'QInputDialog - Name',
                                        'User name:')
        
        if ok and text:
            self.textEdit.append(text)
            
            
    def inputSeason(self):
        items = ['Spring', 'Summer', 'Fall', 'Winter']
        item , ok = QInputDialog.getItem(self, 'QINputDialog - Season',
                                         'Season:', items, 0, False)
        
        if ok and item:
            self.textEdit.append(item)
            
            
    def inputColor(self):
        color = QColorDialog.getColor()
        
        if color.isValid():
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.End)
            
            
    def inputFont(self):
        font, ok = QFontDialog.getFont()
    
        if ok and font:
            # info = QFontInfo(font)
            # self.textEdit.append(info.family() + info.styleName())
            # self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.End)

            
    def openFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File', './', "uifile (*.ui)")

        
        if name[0]:
            with open(name[0], 'r') as file:
                data = file.read()
                self.textEdit.setText(data)

                
    def inputNumber(self):
        text = self.lineEdit.text()
        
        if text.isdigit():
            self.textEdit.setText(text)
        # else:
        #     QMessageBox.warning(self, 'QMessageBox - setText', 'Please enter only numbers. ' )
        #     self.lineEdit.clear()
        else:
            retval = QMessageBox.question(self, 'QMesageBox - question',
                                          'Are you sure to print?',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if retval == QMessageBox.Yes:
                self.textEdit.setText(text)
            else:
                self.lineEdit.clear()
       
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴