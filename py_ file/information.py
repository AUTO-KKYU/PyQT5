from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import QRegExpValidator
 
class MainWindow(QMainWindow):
 
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Line Edit IP Address and Port") # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this accommodation in central widget
 
        grid_layout.addWidget(QLabel("IP Address:", self), 0, 0)
        grid_layout.addWidget(QLabel("Port Number:", self), 1, 0)
 
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"   # Part of the regular expression
        portRange = "(?:[0-9]{1,5})" # Port range (0-65535)
        
        # Regular expression for IP address
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)   
 
        ipLineEdit = QLineEdit()
        ipLineEdit.setValidator(ipValidator)      
        grid_layout.addWidget(ipLineEdit, 0, 1)

        # Regular expression for port number
        portRegex = QRegExp("^" + portRange + "$")
        portValidator = QRegExpValidator(portRegex, self)   

        portLineEdit = QLineEdit()
        portLineEdit.setValidator(portValidator)
        grid_layout.addWidget(portLineEdit, 1, 1)
 
 
if __name__ == "__main__":
    import sys
 
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
