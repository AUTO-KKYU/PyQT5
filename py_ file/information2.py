import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'IP Address Finder'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)

        # Vertical layout
        layout = QVBoxLayout()

        # IP Address label
        self.label = QLabel('Your IP Address: Not Found', self)
        layout.addWidget(self.label)

        # Button to get IP Address
        button = QPushButton('Get IP Address', self)
        button.clicked.connect(self.on_click)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()
    
    def on_click(self):
        ip_address = get_ip_address()
        self.label.setText(f'Your IP Address: {ip_address}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())