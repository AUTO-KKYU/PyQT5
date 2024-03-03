import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QTextEdit, QPushButton
from PyQt5 import uic

from_class = uic.loadUiType("calculator.ui")[0]


class HistoryDialog(QDialog):
    def __init__(self, history_text):
        super().__init__()
        layout = QVBoxLayout()  # 위젯을 수직 방향으로 나열
        self.history_text_edit = QTextEdit()
        self.history_text_edit.setPlainText(history_text)
        
        layout.addWidget(self.history_text_edit)
        self.setLayout(layout)
        self.setWindowTitle("History")


class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.setWindowTitle("Kkyu's Calculator")
        self.setFixedSize(600, 510)
        
        self.setStyleSheet(
            "QLineEdit { border-radius: 10px; }"
            "QGroupBox { background-color: stategray; border: 7px solid seagreen; border-radius: 15px; }"
            "QPushButton { border-radius: 10px;"
            "              background-color: lightgray;"
            "              border: 2px solid gray;"
            "              padding: 5px;"
            "}"
            "QPushButton:pressed {"
            "              background-color: gray;"
            "              border: 2px solid darkgray;"
            "}"
        )
        
        self.history_text = ""
        self.history_dialog = None

        # Numbers
        self.pushButton_0.clicked.connect(self.inputData)  # 0
        self.pushButton_1.clicked.connect(self.inputData)  # 1
        self.pushButton_2.clicked.connect(self.inputData)  # 2
        self.pushButton_3.clicked.connect(self.inputData)  # 3
        self.pushButton_4.clicked.connect(self.inputData)  # 4
        self.pushButton_5.clicked.connect(self.inputData)  # 5
        self.pushButton_6.clicked.connect(self.inputData)  # 6
        self.pushButton_7.clicked.connect(self.inputData)  # 7
        self.pushButton_8.clicked.connect(self.inputData)  # 8
        self.pushButton_9.clicked.connect(self.inputData)  # 9
        self.pushButton_10.clicked.connect(self.inputData) # .
        self.pushButton_22.clicked.connect(self.inputData) # 00
        
        # equal ( = )
        self.pushButton_11.clicked.connect(self.equal)
        
        # delete
        self.pushButton_12.clicked.connect(self.resetAll)   # AE (All Clear)
        self.pushButton_13.clicked.connect(self.resetpart)  # CE (Clear Entry)
        
        # Operator
        self.pushButton_14.clicked.connect(self.plus)  # +
        self.pushButton_15.clicked.connect(self.minus) # -
        self.pushButton_16.clicked.connect(self.multi) # x
        self.pushButton_17.clicked.connect(self.divid) # ÷
        self.pushButton_18.clicked.connect(self.mod)   # mod
    
        # others
        self.pushButton_19.clicked.connect(self.sign)
        self.pushButton_20.clicked.connect(self.parentheses1)
        self.pushButton_21.clicked.connect(self.parentheses2)
        
        # history
        self.pushButton_23.clicked.connect(self.show_history)
        
        # ON/OFF 
        self.pushButton_24.clicked.connect(self.OnMode)
        self.pushButton_25.clicked.connect(self.OffMode)
        
        self.calculator_enabled = True
                
    def OnMode(self):
        self.calculator_enabled = True
        self.setEnabledButtons(True)

    def OffMode(self):
        self.calculator_enabled = False
        self.setEnabledButtons(False)

    def setEnabledButtons(self, enabled):
        buttons = [
            self.pushButton_0, self.pushButton_1, self.pushButton_2, self.pushButton_3,
            self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7,
            self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11,
            self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15,
            self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19,
            self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23 ]
        
        for button in buttons:
            button.setEnabled(enabled)
    
    def resetAll(self):
        if self.calculator_enabled:
            self.initial = ''  
            self.lineEdit.setText(str(self.initial))
        
    def resetpart(self):
        if self.calculator_enabled:
            self.lineEdit.backspace()                
        
    def inputData(self):
        if self.calculator_enabled:
            button = self.sender()
            text = button.text()
            current_text = self.lineEdit.text()
            self.lineEdit.setText(current_text + text)
    
    def plus(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()  
            self.lineEdit.setText(text + " + ")
        
    def minus(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()  
            self.lineEdit.setText(text + " - ")
        
    def multi(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()  
            self.lineEdit.setText(text + " * ")
        
    def divid(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()  
            self.lineEdit.setText(text + " / ")
        
    def mod(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()  
            self.lineEdit.setText(text + " % ")
    
    def parentheses1(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()
            self.lineEdit.setText(text + " ( ")
    
    def parentheses2(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()
            self.lineEdit.setText(text + " ) ")
        
    def sign(self):
        if self.calculator_enabled:
            text = self.lineEdit.text()
            if text:
                if text[0] == '-':
                    self.lineEdit.setText(text[1:])
                else:
                    self.lineEdit.setText('-' + text)
                
    def equal(self):
        if self.calculator_enabled:
            equation = self.lineEdit.text()  
    
        # 소괄호가 적절하게 사용되었는지 확인
        if equation.count('(') != equation.count(')'):
            self.lineEdit.setText("Syntax ERROR")
    
        # 연산자들이 연속적으로 적혀있는지 확인
        if any(op1 + op2 in equation for op1, op2 in [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/'), ('%', '%')]):
            self.lineEdit.setText("Syntax ERROR")
            
        # point가 연속적으로 적혀있는지 확인
        if any(x1 + x2 in equation for x1, x2 in [('.', '.')]):
            self.lineEdit.setText("Math ERROR")
            
            
        try:
            ans = eval(equation)
            self.lineEdit.setText(str(ans))
            self.history_text += equation + " = " + str(ans) + "\n"
            
        except ZeroDivisionError:
            self.lineEdit.setText("Math ERROR")
            
        except Exception:
            self.lineEdit.setText("Syntax ERROR")
            
            
    def show_history(self):
        if not self.history_dialog:
            self.history_dialog = HistoryDialog(self.history_text)
        self.history_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec())
