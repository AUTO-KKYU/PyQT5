import sys
import mysql.connector
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QFileDialog, QDateEdit, QMessageBox
from PyQt5.QtCore import *


from_class = uic.loadUiType("/home/kkyu/amr_ws/QT/Quiz.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
                
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnSearch.clicked.connect(self.Select_data)
        self.pushButton.clicked.connect(self.OpenFile)
        self.pushButton2.clicked.connect(self.SaveFile)

        # start
        default_date = QDate(1970, 6, 7)
        self.editBirthday.setDate(default_date)
        
        # end
        default_date_2 = QDate(1999, 5, 4)
        self.editBirthday_2.setDate(default_date_2)
        

        sex_index = ['M','F']
        for x in sex_index:
            self.editSex.addItem(str(x))
            
        job_index = ['가수','MC','개그맨','영화배우','텔런트','모델']
        for x in job_index:
            self.editJobTitle.addItem(str(x))
            
        agency_index = ['EDAM엔터테이먼트','나무엑터스','YG엔터테이먼트','안테나']
        for x in agency_index:
            self.editAgency.addItem(str(x))
            
        self.editSex.currentIndexChanged.connect(self.Select_Sex)
        self.editJobTitle.currentIndexChanged.connect(self.Select_Job)
        self.editAgency.currentIndexChanged.connect(self.Select_Agency)

    def Select_data(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="7500",
                database="amrbase"
            )
            
            cursor = self.conn.cursor(buffered=True)
            cursor.execute("SELECT * FROM celeb")

            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            
    
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    
            result = "{}".format(self.conn.server_host)
            self.lineEdit.setText(result)
            
            result2 = "{}".format(self.conn.server_port)
            self.lineEdit_2.setText(result2)
                    
        except mysql.connector.Error as e:
            print("Error:", e)
            print("Failed to fetch data from database.")
            print("Check your connection settings and database.")
      
      
    def OpenFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File', '/home/kkyu/sql_backup', "uifile (*.sql *.csv)")

        if name[0]:
            with open(name[0], 'r') as file:
                self.tableWidget = QTableWidgetItem()
                data = file.read()
                self.tableWidget.loadFromData(data)
                self.textEdit.setText(data)
                
    
    def SaveFile(self):
        # 파일 형식자도 같이 적어줘야 함
        filename = QFileDialog.getSaveFileName(self, 'save image', './', 'img')
        self.tableWidget.save(filename[0])
    
                   
    def Select_Sex(self):
        selected_sex = self.editSex.currentText()
        query = "SELECT * FROM celeb WHERE sex = %s"
        self.execute_query_with_filter(query, (selected_sex,))


    def Select_Job(self):
        selected_job = self.editJobTitle.currentText()
        query = "SELECT * FROM celeb WHERE job_title = %s"
        self.execute_query_with_filter(query, (selected_job,))


    def Select_Agency(self):
        selected_agency = self.editAgency.currentText()
        query = "SELECT * FROM celeb WHERE agency = %s"
        self.execute_query_with_filter(query, (selected_agency,))

    def execute_query_with_filter(self, query, params):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="7500",
                database="amrbase"
            )
            cursor = self.conn.cursor(buffered=True)
            cursor.execute(query, params)

            result = cursor.fetchall()
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mysql.connector.Error as e:
            print("Error:", e)
            print("Failed to fetch data from database.")
            print("Check your connection settings and database.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())