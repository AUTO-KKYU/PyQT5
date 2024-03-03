import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 

from_class = uic.loadUiType("Test2.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test2")
        
        self.count = 0
        self.sum = 0
        self.avg = 0
        self.string = ''
                       
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.write)
        
        self.label.setText(str(self.count))
        self.label_2.setText(str(self.sum))
        self.label_6.setText(str(self.avg))
        self.label_7.setText(self.string)
        
        self.lineEdit_2.textChanged.connect(self.changed)
            
    def changed(self):
        self.lineEdit_3.setText(self.lineEdit_2.text())
                
    def write(self):
        self.label_7.setText(self.lineEdit.text())
        
    def buttonClicked(self):
        self.count += 1
        self.sum += self.count
        self.avg += self.sum / self.count
        
        self.label.setText(str(self.count))
        self.label_2.setText(str(self.sum))
        self.label_6.setText(str(self.avg))
        
    def reset(self):
        self.count = 0
        self.sum = 0
        self.avg = 0
        
        self.label.setText(str(self.count))
        self.label_2.setText(str(self.sum))
        self.label_6.setText(str(self.avg))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec())