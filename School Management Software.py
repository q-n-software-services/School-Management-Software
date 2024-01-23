from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSpinBox, QDialog, QListWidget, QLabel, QListWidgetItem, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon, QPen, QFont


from PyQt5 import QtCore, QtGui
import sqlite3

total_sale = 0.0
bill = 0.0
payed = 0.0
balance = 12.12

cust_list = []
customer_count = 1



class Item:
    def __init__(self, sr_num, name, price, details, stock, icon_link, sale):
        self.sr_num = sr_num
        self.name = name
        self.price = price
        self.details = details
        self.stock = stock
        self.icon_link = icon_link
        self.sale = sale



item_one = Item(1, "first item", 12, "bla bla bla", 55, "N/A", 0)
Second_item = Item(2, "second item", 15, "kdlkndlkn", 60, "N/A", 0)
Third_Item = Item(3, "Third Item", 14, "wehdouegyfevc", 45, "N/A", 0)
Fourth_Item = Item(4, "Fourth Item", 18, "owidhweocb", 70, "N/A", 0)
Fifth_Item = Item(5, "Fifth Item", 17, "wiycgewghowlknx",80, "N/A", 0)
Sixth_item = Item(6, "Sixth Item", 48, "pweojcwnoksclksh0",80, "N/A", 0)

conn = sqlite3.connect("SchoolData.sqlite")
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS POS''')

cur.execute('''
CREATE TABLE POS (sr_num INTEGER, name TEXT, price INTEGER, Sale INTEGER, Stock INTEGER)''')


cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (item_one.sr_num, item_one.name, item_one.price, item_one.sale, item_one.stock))
cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (Second_item.sr_num, Second_item.name, Second_item.price, Second_item.sale, Second_item.stock))
cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (Third_Item.sr_num, Third_Item.name, Third_Item.price,Third_Item.sale, Third_Item.stock))
cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (Fourth_Item.sr_num, Fourth_Item.name, Fourth_Item.price, Fourth_Item.sale, Fourth_Item.stock))
cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (Fifth_Item.sr_num, Fifth_Item.name, Fifth_Item.price, Fifth_Item.sale, Fifth_Item.stock))
cur.execute('INSERT INTO POS (sr_num, name, price, Sale, Stock) VALUES (?, ?, ?, ?, ?)', (Sixth_item.sr_num, Sixth_item.name, Sixth_item.price, Sixth_item.sale, Sixth_item.stock))

class window_example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1400, 700)
        # self.setFixedWidth(1350)
        # self.setFixedHeight(700)
        self.setWindowTitle("SCHOOL Management Software")
        self.setWindowIcon(QIcon('masjid.ico'))
        self.setStyleSheet('background-color:rgb(212, 212, 212)')
        self.create_buttons()
        self.show()



    def create_buttons(self):
        btn1 = QPushButton("Time Tables", self)
        btn1.setGeometry(50, 424, 100, 100)
        btn1.setStyleSheet('background-color:Red')
        btn1.setIcon(QIcon("masjid.ico"))
        btn1.setIconSize(QtCore.QSize(40, 80))
        btn1.clicked.connect(self.btnm1_clicked)

        btn2 = QPushButton("Student Data", self)
        btn2.setGeometry(151, 424, 100, 100)
        btn2.setStyleSheet("background-color:Orange")
        btn2.setIcon(QIcon("masjid.ico"))
        btn2.setIconSize(QtCore.QSize(40, 80))
        btn2.clicked.connect(self.btnm2_clicked)

        btn3 = QPushButton(" Attendance", self)
        btn3.setGeometry(252, 424, 100, 100)
        btn3.setStyleSheet("background-color:Yellow")
        btn3.setIcon(QIcon("masjid.ico"))
        btn3.setIconSize(QtCore.QSize(40, 80))
        btn3.clicked.connect(self.btnm3_clicked)

        btn4 = QPushButton("Logout", self)
        btn4.setGeometry(353, 424, 100, 100)
        btn4.setStyleSheet('background-color:Green')
        btn4.setIcon(QIcon("masjid.ico"))
        btn4.setIconSize(QtCore.QSize(40, 80))
        btn4.clicked.connect(self.btn4_clicked)


        btn5 = QPushButton("Teachers Data", self)
        btn5.setGeometry(50, 525, 100, 100)
        btn5.setStyleSheet('background-color:Blue')
        btn5.setIcon(QIcon("masjid.ico"))
        btn5.setIconSize(QtCore.QSize(40, 80))
        btn5.clicked.connect(self.btnm5_clicked)


        btn6 = QPushButton("Faculty\n Attendance", self)
        btn6.setGeometry(151, 525, 100, 100)
        btn6.setStyleSheet('background-color:Indigo')
        btn6.setIcon(QIcon("masjid.ico"))
        btn6.setIconSize(QtCore.QSize(40, 80))
        btn6.clicked.connect(self.btnm6_clicked)


        btn7 = QPushButton("Reports", self)
        btn7.setGeometry(252, 525, 100, 100)
        btn7.setStyleSheet('background-color:Violet')
        btn7.setIcon(QIcon("masjid.ico"))
        btn7.setIconSize(QtCore.QSize(40, 80))
        btn7.clicked.connect(self.btnm4_clicked)



        btn8 = QPushButton("Finance\n Management", self)
        btn8.setGeometry(353, 525, 100, 100)
        btn8.setStyleSheet('background-color:white')
        btn8.setIcon(QIcon("masjid.ico"))
        btn8.setIconSize(QtCore.QSize(40, 80))
        btn8.clicked.connect(self.btn8_clicked)

        self.list_main = QListWidget()
        self.list_main.setGeometry(931, 89, 422, 590)
        self.list_main.setStyleSheet("background-color:pink")
        self.list_main.setFont(QFont('Sanserif', 14))
        self.list_main.insertItem(0, '\tData Retrieved from Database comes here ')
        self.list_main.insertItem(2, '\te.g.  list of students in a class etc ')

        vbx1 = QHBoxLayout()

        label1 = QLabel("\tABC School Private Limited \t\t\t\t\t")
        label1.setFont(QFont("Sanserif", 18))
        vbx1.addWidget(label1)

        vbx2 = QHBoxLayout()
        label2 = QLabel("\tYour Tagline/ Mission/ Vision ")
        label2.setFont(QFont("Sanserif", 18))
        vbx2.addWidget(label2)



        vbx4 = QGridLayout()
        vbx4.addWidget(btn1, 0, 0)
        vbx4.addWidget(btn2, 0, 1)
        vbx4.addWidget(btn3, 0, 2)
        vbx4.addWidget(btn4, 0, 3)
        vbx4.addWidget(btn5, 1, 0)
        vbx4.addWidget(btn6, 1, 1)
        vbx4.addWidget(btn7, 1, 2)
        vbx4.addWidget(btn8, 1, 3)
        xvbox = QVBoxLayout()
        xvbox.addLayout(vbx1)
        xvbox.addLayout(vbx2)
        dhbox = QHBoxLayout()
        dhbox.addLayout(vbx4)
        label3 = QLabel("")
        dhbox.addWidget(label3)
        xvbox.addLayout(dhbox)

        hbox = QHBoxLayout()
        hbox.addLayout(xvbox)

        hbox.addWidget(self.list_main)

        self.setLayout(hbox)









    def btnm1_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Time Tables")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("1st Class")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('burger.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func12)

        btnx2 = QPushButton("2nd Class")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('burger.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func13)

        btnx3 = QPushButton("3rd Class")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('burger.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func14)

        btnx4 = QPushButton("4th Class")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('burger.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func15)

        btnx5 = QPushButton("5th Class")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('burger.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func16)

        btnx6 = QPushButton("6th Class")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('burger.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func17)

        btnx7 = QPushButton("7th Class")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('burger.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func18)

        btnx8 = QPushButton("8th Class")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('burger.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func19)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func12(self):
        self.btn1_clicked(2)

    def value_func13(self):
        self.btn1_clicked(3)

    def value_func14(self):
        self.btn1_clicked(4)

    def value_func15(self):
        self.btn1_clicked(5)

    def value_func16(self):
        self.btn1_clicked(6)

    def value_func17(self):
        self.btn1_clicked(7)

    def value_func18(self):
        self.btn1_clicked(8)

    def value_func19(self):
        self.btn1_clicked(9)






    def btnm2_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Student Data")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("John")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('burger.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func22)

        btnx2 = QPushButton("Mathew")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('burger.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func23)

        btnx3 = QPushButton("James")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('burger.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func24)

        btnx4 = QPushButton("Arnold")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('burger.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func25)

        btnx5 = QPushButton("George")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('burger.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func26)

        btnx6 = QPushButton("Donald")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('burger.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func27)

        btnx7 = QPushButton("Charles")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('burger.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func28)

        btnx8 = QPushButton("Simpson")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('burger.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func29)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func22(self):
        self.btn2_clicked(2)

    def value_func23(self):
        self.btn2_clicked(3)

    def value_func24(self):
        self.btn2_clicked(4)

    def value_func25(self):
        self.btn2_clicked(5)

    def value_func26(self):
        self.btn2_clicked(6)

    def value_func27(self):
        self.btn2_clicked(7)

    def value_func28(self):
        self.btn2_clicked(8)

    def value_func29(self):
        self.btn2_clicked(9)





    def btnm3_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Attendance")
        settings_dialog.setWindowIcon(QIcon("masjid.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("Class 1")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('masjid.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func32)

        btnx2 = QPushButton("Class 2")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('masjid.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func33)

        btnx3 = QPushButton("Class 3")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('masjid.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func34)

        btnx4 = QPushButton("Class 4")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('masjid.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func35)

        btnx5 = QPushButton("Class 5")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('masjid.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func36)

        btnx6 = QPushButton("Class 6")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('masjid.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func37)

        btnx7 = QPushButton("Class 7")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('masjid.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func38)

        btnx8 = QPushButton("Class8")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('masjid.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func39)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func32(self):
        self.btn3_clicked(2)

    def value_func33(self):
        self.btn3_clicked(3)

    def value_func34(self):
        self.btn3_clicked(4)

    def value_func35(self):
        self.btn3_clicked(5)

    def value_func36(self):
        self.btn3_clicked(6)

    def value_func37(self):
        self.btn3_clicked(7)

    def value_func38(self):
        self.btn3_clicked(8)

    def value_func39(self):
        self.btn3_clicked(9)




    def btnm4_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Reports")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("1st Class")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('masjid.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func42)

        btnx2 = QPushButton("2nd Class")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('masjid.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func43)

        btnx3 = QPushButton("3rd Class")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('masjid.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func44)

        btnx4 = QPushButton("4th Class")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('masjid.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func45)

        btnx5 = QPushButton("5th Class")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('masjid.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func46)

        btnx6 = QPushButton("6th Class")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('masjid.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func47)

        btnx7 = QPushButton("7th Class")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('masjid.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func48)

        btnx8 = QPushButton("8th Class")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('masjid.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func49)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func42(self):
        self.btn4_clicked(2)

    def value_func43(self):
        self.btn4_clicked(3)

    def value_func44(self):
        self.btn4_clicked(4)

    def value_func45(self):
        self.btn4_clicked(5)

    def value_func46(self):
        self.btn4_clicked(6)

    def value_func47(self):
        self.btn4_clicked(7)

    def value_func48(self):
        self.btn4_clicked(8)

    def value_func49(self):
        self.btn4_clicked(9)



    def btnm5_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Teachers Data")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("Biology Teacher")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('burger.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func52)

        btnx2 = QPushButton("Chemistry Teacher")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('burger.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func53)

        btnx3 = QPushButton("Physics Teacher")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('burger.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func54)

        btnx4 = QPushButton("Mathematics Teacher")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('burger.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func55)

        btnx5 = QPushButton("Computer Science\nTeacher")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('burger.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func56)

        btnx6 = QPushButton("English Teacher")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('burger.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func57)

        btnx7 = QPushButton("Economics Teacher")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('burger.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func58)

        btnx8 = QPushButton("Accounting Teacher")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('burger.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func59)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func52(self):
        self.btn5_clicked(2)

    def value_func53(self):
        self.btn5_clicked(3)

    def value_func54(self):
        self.btn5_clicked(4)

    def value_func55(self):
        self.btn5_clicked(5)

    def value_func56(self):
        self.btn5_clicked(6)

    def value_func57(self):
        self.btn5_clicked(7)

    def value_func58(self):
        self.btn5_clicked(8)

    def value_func59(self):
        self.btn5_clicked(9)



    def btnm6_clicked(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Faculty\n Attendance")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(300, 75, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("ID 1")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('burger.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)
        btnx1.clicked.connect(self.value_func62)

        btnx2 = QPushButton("ID 2")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('burger.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)
        btnx2.clicked.connect(self.value_func63)

        btnx3 = QPushButton("ID 3")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('burger.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 0, 2)
        btnx3.clicked.connect(self.value_func64)

        btnx4 = QPushButton("ID 4")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('burger.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 0)
        btnx4.clicked.connect(self.value_func65)

        btnx5 = QPushButton("ID 5")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('burger.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 1, 1)
        btnx5.clicked.connect(self.value_func66)

        btnx6 = QPushButton("ID 6")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('burger.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 1, 2)
        btnx6.clicked.connect(self.value_func67)

        btnx7 = QPushButton("ID 7")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('burger.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 2, 0)
        btnx7.clicked.connect(self.value_func68)

        btnx8 = QPushButton("ID 8")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('burger.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 2, 1)
        btnx8.clicked.connect(self.value_func69)



        Value_Box = QLineEdit()
        Value_Box.setStyleSheet("color:white")
        vbox2 = QVBoxLayout()
        vbox2.addWidget(Value_Box)

        btn_ok = QPushButton("OK")
        btn_ok.setStyleSheet("background-color:pink")

        vbox2.addWidget(btn_ok)

        vbox.addLayout(vbox2, 2, 2)






        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()


    def value_func62(self):
        self.btn6_clicked(2)

    def value_func63(self):
        self.btn6_clicked(3)

    def value_func64(self):
        self.btn6_clicked(4)

    def value_func65(self):
        self.btn6_clicked(5)

    def value_func66(self):
        self.btn6_clicked(6)

    def value_func67(self):
        self.btn6_clicked(7)

    def value_func68(self):
        self.btn6_clicked(8)

    def value_func69(self):
        self.btn6_clicked(9)



    def btn1_clicked(self, value):
        global total_sale
        global cust_list
        global bill

        if not value:
            value = 1
        print("Button One Clicked", value, "times")
        total_sale = total_sale + (value * item_one.price)
        bill = bill + (value * item_one.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, item_one.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, item_one.name))
        cust_list.append(item_one.name + "\t\t    " + str(value))
        conn.commit()


    def btn2_clicked(self, value):
        global total_sale
        global cust_list
        global bill
        if not value:
            value = 1
        print("Button TWO Clicked", value, "times")
        total_sale = total_sale + (value * Second_item.price)
        bill = bill + (value * Second_item.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, Second_item.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, Second_item.name))
        cust_list.append(Second_item.name + "\t\t    " + str(value))
        conn.commit()


    def btn3_clicked(self, value):
        global total_sale
        global cust_list
        global bill
        if not value:
            value = 1
        print("Button Three Clicked", value, "times")
        total_sale = total_sale + (value * Third_Item.price)
        bill = bill + (value * Third_Item.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, Third_Item.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, Third_Item.name))
        cust_list.append(Third_Item.name + "\t\t    " + str(value))
        conn.commit()

    def btn4_clicked(self, value):
        global total_sale
        global cust_list
        global bill
        if not value:
            value = 1
        print("Button Four Clicked", value, "times")
        total_sale = total_sale + (value * Fourth_Item.price)
        bill = bill + (value * Fourth_Item.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, Fourth_Item.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, Fourth_Item.name))
        cust_list.append(Fourth_Item.name + "\t\t    " + str(value))
        conn.commit()

    def btn5_clicked(self, value):
        global total_sale
        global cust_list
        global bill
        if not value:
            value = 1
        print("Button Five Clicked", value, "times")
        total_sale = total_sale + (value * Fifth_Item.price)
        bill = bill + (value * Fifth_Item.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, Fifth_Item.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, Fifth_Item.name))
        cust_list.append(Fifth_Item.name + "\t\t    " + str(value))
        conn.commit()

    def btn6_clicked(self, value):
        global total_sale
        global cust_list
        global bill
        if not value:
            value = 1
        print("Button Six Clicked", value, "times")
        total_sale = total_sale + (value * Sixth_item.price)
        bill = bill + (value * Sixth_item.price)
        cur.execute('UPDATE POS SET Stock = Stock - ? WHERE Name = ?', (value, Sixth_item.name))
        cur.execute('UPDATE POS SET Sale = Sale + ? WHERE Name = ?', (value, Sixth_item.name))
        cust_list.append(Sixth_item.name + "\t\t    " + str(value))
        conn.commit()

    def btn7_clicked(self):
        global total_sale
        global cust_list
        global bill
        global balance
        global payed

        CheckOut_dialog = QDialog()
        CheckOut_dialog.setModal(True)
        CheckOut_dialog.setStyleSheet("background-color:blue")
        CheckOut_dialog.setWindowTitle("            Check Out")
        CheckOut_dialog.setWindowIcon(QIcon("burger.ico"))
        CheckOut_dialog.setGeometry(600, 150, 400, 300)
        vbox = QVBoxLayout()
        list_widget = QListWidget()
        list_widget.setFont(QFont("Sanserif", 17))
        list_widget.setStyleSheet("background-color:pink")
        i = 0
        for j in cust_list:
            list_widget.insertItem(i, "    " + j)
            i = i + 1

        vbox.addWidget(list_widget)

        my_label = QLabel("hello")
        my_label.setStyleSheet("background-color:violet")
        my_label.setFont(QFont("Sanserif", 22))
        my_label.setText("   Bill   =\t\t" + str(bill))

        vbox.addWidget(my_label)




        line_edit = QLineEdit()
        line_edit.setStyleSheet("background-color:white")
        vbox.addWidget(line_edit)


        '''label2 = QLabel()
        label2.setStyleSheet("background-color:yellow")
        label2.setFont(QFont("Sanserif", 22))
        label2.setText(str(balance))

        btnco = QPushButton("\tSubmit12")
        btnco.setStyleSheet("background-color:red")
        btnco.setFont(QFont("Sanserif", 14))
        vbox.addWidget(btnco)
        btnco.clicked.connect(self.payment_recieved)

        label2.setText(str(balance))




        vbox.addWidget(label2)'''
        CheckOut_dialog.setLayout(vbox)
        CheckOut_dialog.exec_()











        # payment = self.line_edit.text()
        # payed = int(payment)





    def btn8_clicked(self):

        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:black")
        settings_dialog.setWindowTitle("Settings")
        settings_dialog.setWindowIcon(QIcon("burger.ico"))
        settings_dialog.setGeometry(700, 150, 400, 300)
        vbox = QGridLayout()
        btnx1 = QPushButton("ADD ")
        btnx1.setStyleSheet("background-color:white")
        btnx1.setGeometry(0, 0, 120, 120)
        btnx1.setIcon(QIcon('burger.ico'))
        btnx1.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx1, 0, 0)

        btnx2 = QPushButton("REMOVE")
        btnx2.setStyleSheet("background-color:violet")
        btnx2.setGeometry(120, 0, 120, 120)
        btnx2.setIcon(QIcon('burger.ico'))
        btnx2.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx2, 0, 1)

        btnx3 = QPushButton("CHANGE It")
        btnx3.setStyleSheet("background-color:indigo")
        btnx3.setGeometry(0, 120, 120, 120)
        btnx3.setIcon(QIcon('burger.ico'))
        btnx3.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx3, 1, 0)

        btnx4 = QPushButton("Change Th")
        btnx4.setStyleSheet("background-color:blue")
        btnx4.setGeometry(120, 120, 120, 120)
        btnx4.setIcon(QIcon('burger.ico'))
        btnx4.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx4, 1, 1)

        btnx5 = QPushButton("Update Inv")
        btnx5.setStyleSheet("background-color:green")
        btnx5.setGeometry(0, 240, 120, 120)
        btnx5.setIcon(QIcon('burger.ico'))
        btnx5.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx5, 2, 0)

        btnx6 = QPushButton("SIX")
        btnx6.setStyleSheet("background-color:yellow")
        btnx6.setGeometry(120, 240, 120, 120)
        btnx6.setIcon(QIcon('burger.ico'))
        btnx6.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx6, 2, 1)

        btnx7 = QPushButton("SEVEN")
        btnx7.setStyleSheet("background-color:orange")
        btnx7.setGeometry(0, 360, 120, 120)
        btnx7.setIcon(QIcon('burger.ico'))
        btnx7.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx7, 3, 0)

        btnx8 = QPushButton("EIGHT")
        btnx8.setStyleSheet("background-color:red")
        btnx8.setGeometry(120, 360, 120, 120)
        btnx8.setIcon(QIcon('burger.ico'))
        btnx8.setIconSize(QtCore.QSize(120, 120))
        vbox.addWidget(btnx8, 3, 1)

        settings_dialog.setLayout(vbox)
        settings_dialog.exec_()









app = QApplication(sys.argv)
window = window_example()
window.show()
sys.exit(app.exec_())
