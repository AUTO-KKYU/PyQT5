import sys
from PyQt5. QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
import urllib.request 
import xml.etree.ElementTree as et


from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Test9.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(700, 570)
        
        self.labelValue.setStyleSheet("border-radius: 5px;"
                          "border: 1px solid gray;"
                          "background-color: #BBDEFB")
        
        self.labelValue2.setStyleSheet("border-radius: 5px;"
                          "border: 1px solid gray;"
                          "background-color: #FF0000")

        self.labelValue3.setStyleSheet("border-radius: 5px;"
                          "border: 1px solid gray;"
                          "background-color: #E1BEE7")
           
        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()
        
        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))
        
        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)
        
        self.dial.setRange(min, max)
        self.dial.setSingleStep(step)
        
        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinbox)
        self.slider.valueChanged.connect(self.changeSlider)
        self.dial.valueChanged.connect(self.changeDial)
        self.btnOpen.clicked.connect(self.fileOpen)
        self.btnSave.clicked.connect(self.fileSave)


    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()
        
        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))
        
        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))
        
        self.dial.setRange(int(min), int(max))
        self.dial.setSingleStep(int(step))
        
        
    def changeSpinbox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.slider.setValue(actualValue)
        self.dial.setValue(actualValue)
        self.updateImageSize(actualValue)
        
        
    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.spinBox.setValue(actualValue)
        self.dial.setValue(actualValue)
        self.updateImageSize(actualValue)


    def changeDial(self):
        actualValue = self.dial.value()
        self.labelValue3.setText(str(actualValue))
        self.spinBox.setValue(actualValue)
        self.slider.setValue(actualValue)
        self.updateImageSize(actualValue)

        
    def updateImageSize(self, size):
        if self.pixmap:
            scaled_pixmap = self.pixmap.scaled(size, size, Qt.KeepAspectRatio)
            self.labelPixmap.setPixmap(scaled_pixmap)
            self.labelPixmap.setAlignment(Qt.AlignCenter)
            self.labelSize.setText(f"{size}x{size}")


    def fileOpen(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', '/home/kkyu/amr_ws/QT/data', "img (*.png *.webp *.JPEG *.jpg *.bmp *.tif)")

        if name:
            with open(name, 'rb') as file:
                self.pixmap = QPixmap()
                data = file.read()
                self.pixmap.loadFromData(data)

                # Display the pixmap (default)
                self.labelPixmap.setPixmap(self.pixmap.scaled(self.labelPixmap.width(), self.labelPixmap.height()))
                self.labelSize.setText(f"{self.pixmap.width()} x {self.pixmap.height()}")  # 이미지의 너비와 높이를 보여줌
                self.labelSize.setAlignment(Qt.AlignCenter)

                
    def fileSave(self):
        # 파일 형식자도 같이 적어줘야 함
        filename = QFileDialog.getSaveFileName(self, 'save image', './', 'img')
        self.pixmap.save(filename[0])
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 프로그램 실행
    myWindows = WindowClass()     # 화면 클래스 생성
    myWindows.show()              # 프로그램 화면 보이기
    sys.exit(app.exec())          # 프로그램을 종료까지 동작시킴