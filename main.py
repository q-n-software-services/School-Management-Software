# Importing built-in functions from libraries
import glob
import math
import pandas as pd
from PyQt5.QtWidgets import QApplication, QDialog,QComboBox, QLineEdit,QDateEdit, QToolButton, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber, QMessageBox, QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon, QPainter as qp
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer, QLocale, Qt, QDateTime
import time
from random import randint
import sqlite3, sys, os
Class = 'None'
done = False
panel_status = False
panel_status2 = False
maleTeacher = 0
femaleTeacher = 0
currentStudent = ''
permission = False
# Database setup and related stuff of SQLite3
# conn = sqlite3.connect("wrestling_predictor.sqlite")
# cur = conn.cursor()

# cur.execute('''DROP TABLE IF EXISTS Player_Data''')

# cur.execute('''CREATE TABLE Player_Data (id INTEGER, name TEXT, rating REAL)''')

# cur.execute('INSERT INTO Player_Data (id, name, rating) VALUES (?, ?, ?)', (3, "vacant_id", 12.12))
# cur.execute('INSERT INTO Player_Data (id, name, rating) VALUES (?, ?, ?)', (player1_id, player1_name, player1_rating))
# cur.execute('INSERT INTO Player_Data (id, name, rating) VALUES (?, ?, ?)', (player2_id, player2_name, player2_rating))
# conn.commit()



'''now = datetime.datetime.now()
if str(now.year) == '2023' and str(now.month) == '7' and str(now.day) == "3":
    pass
else:
    exit()'''



widgets = []

# Below is the GUI code written using PyQt5 library of PYTHON
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.showFullScreen()

        self.setWindowTitle("Drop_Down_List_PyQt5")
        self.setWindowIcon(QIcon("School Management Icons/university_library.ico"))

        self.create_combo_box()

    def create_combo_box(self):
        self.login()
        global permission
        global player1_id
        global player1_name
        global player1_rating
        global player1_match_points
        global player2_id
        global player2_name
        global player2_rating
        global player2_match_points
        global prediction_show
        global cur
        global conn


        self.vbox = QVBoxLayout()
        self.vboxMain = QVBoxLayout()


# labels are used to display text and data on screen

        self.label_title1 = QLabel("Admin Dashboard")
        self.label_title1.setAlignment(Qt.AlignCenter)
        self.label_title1.setFont(QFont("Sanserif", 22))
        self.label_title1.setStyleSheet("background-color:white")
        self.label_title1.setFixedHeight(63)

        self.label = QLabel()
        now = datetime.datetime.now()
        day1 = now.weekday()
        if day1 == 0:
            day1 = 'Monday'
        elif day1 == 1:
            day1 = 'Tuesday'
        elif day1 == 2:
            day1 = 'Wednesday'
        elif day1 == 3:
            day1 = 'Thursday'
        elif day1 == 4:
            day1 = 'Friday'
        elif day1 == 5:
            day1 = 'Saturday'
        elif day1 == 6:
            day1 = 'Sunday'
        self.label.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setFont(QFont("times new roman", 22))
        self.label.setFixedHeight(44)
        self.label.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vboxMain.addWidget(self.label) # lightgray, khaki, lightblue, lightyellow

        self.vbox_side = QVBoxLayout()
        self.vbox_side_content = QVBoxLayout()

        self.btn110 = QPushButton(' Dashboard ')
        self.btn110.setFont(QFont("Sanserif", 16))
        self.btn110.setFixedWidth(227)
        self.btn110.clicked.connect(self.showDashboard)
        # self.btn110.clicked.connect(self.new)

        self.btn110.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn110)
        self.btn110.hide()

        self.btn111 = QPushButton('Student Admission')
        self.btn111.setFont(QFont("Sanserif", 16))
        self.btn111.setFixedWidth(227)
        self.btn111.clicked.connect(self.showStudentAdmission)
        self.btn111.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn111)
        self.btn111.hide()

        self.btn112 = QPushButton('Teaching Staff')
        self.btn112.setFont(QFont("Sanserif", 16))
        self.btn112.setFixedWidth(227)
        self.btn112.clicked.connect(self.showTeachingStaff)
        self.btn112.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn112)
        self.btn112.hide()


        self.btn113 = QPushButton('Non-Teaching Staff ')
        self.btn113.setFont(QFont("Sanserif", 16))
        self.btn113.setFixedWidth(227)
        self.btn113.clicked.connect(self.showNonTeachingStaff)
        self.btn113.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn113)
        self.btn113.hide()


        self.btn114 = QPushButton('Marks')
        self.btn114.setFont(QFont("Sanserif", 16))
        self.btn114.setFixedWidth(227)
        self.btn114.clicked.connect(self.showMarks)
        self.btn114.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn114)
        self.btn114.hide()

        self.btn115 = QPushButton('Students Attendance')
        self.btn115.setFont(QFont("Sanserif", 16))
        self.btn115.setFixedWidth(227)
        self.btn115.clicked.connect(self.showStudentAttendance)
        self.btn115.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn115)
        self.btn115.hide()

        self.btn116 = QPushButton('Staff Attendance')
        self.btn116.setFont(QFont("Sanserif", 16))
        self.btn116.setFixedWidth(227)
        self.btn116.clicked.connect(self.showStaffAttendance)
        self.btn116.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn116)
        self.btn116.hide()

        self.btn117 = QPushButton('Payment / Finances')
        self.btn117.setFont(QFont("Sanserif", 16))
        self.btn117.setFixedWidth(227)
        self.btn117.clicked.connect(self.showFinances)
        self.btn117.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn117)
        self.btn117.hide()

        self.btn118 = QPushButton('Class Timetable')
        self.btn118.setFont(QFont("Sanserif", 16))
        self.btn118.setFixedWidth(227)
        self.btn118.clicked.connect(self.showClassTimetable)
        self.btn118.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn118)
        self.btn118.hide()

        self.btn119 = QPushButton('Things To Do')
        self.btn119.setFont(QFont("Sanserif", 16))
        self.btn119.setFixedWidth(227)
        self.btn119.clicked.connect(self.showThingsToDo)
        self.btn119.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn119)
        self.btn119.hide()

        self.btn1199 = QPushButton('Others')
        self.btn1199.setFont(QFont("Sanserif", 16))
        self.btn1199.setFixedWidth(227)
        self.btn1199.clicked.connect(self.showOthers)
        self.btn1199.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn1199)
        self.btn1199.hide()

        self.btn119922 = QPushButton('Change Password')
        self.btn119922.setFont(QFont("Sanserif", 16))
        self.btn119922.setFixedWidth(227)
        self.btn119922.clicked.connect(self.changePassword)
        self.btn119922.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.vbox_side_content.addWidget(self.btn119922)
        self.btn119922.hide()




        # creating a timer object
        self.timer = QTimer()

        # adding action to timer
        self.timer.timeout.connect(self.changeTime)

        # update the timer every tenth second
        self.timer.start(1000)

        # creating a timer object
        self.timercheck = QTimer()

        # adding action to timer
        self.timercheck.timeout.connect(self.check)

        # update the timer every tenth second
        self.timercheck.start(500)

        self.btn_close = QPushButton("CLOSE")
        self.btn_close.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:red; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.btn_close.setFont(QFont("Sanserif", 12))
        self.btn_close.setFixedHeight(60)
        self.btn_close.clicked.connect(self.closew)

        self.btn_minimize = QPushButton("MINIMIZE")
        self.btn_minimize.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.btn_minimize.setFont(QFont("Sanserif", 12))
        self.btn_minimize.setFixedHeight(60)
        self.btn_minimize.clicked.connect(self.minimizew)

        self.btn_removep = QPushButton("REMOVE PLAYER")
        self.btn_removep.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:pink; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.btn_removep.setFont(QFont("Sanserif", 12))
        self.btn_removep.setFixedHeight(60)
        # self.btn_removep.clicked.connect(self.remove_player)

        self.btn_addp = QPushButton("Contact Developers")
        self.btn_addp.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:springgreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.btn_addp.setFont(QFont("Sanserif", 12))
        self.btn_addp.setFixedHeight(60)
        self.btn_addp.pressed.connect(self.showOthers)
        # self.btn_addp.clicked.connect(lambda: time.sleep(1))
        self.btn_addp.released.connect(lambda: self.label_title2.setText('Contact Developers'))
        self.btn_addp.released.connect(lambda: self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:springgreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);"))


        self.vbox.addWidget(self.label_title1)

        self.hboxRow1 = QHBoxLayout()

        self.studentAdmission = QPushButton("Student\nAdmission")
        self.studentAdmission.setFont(QFont("times new roman", 16))
        self.studentAdmission.setIcon(QIcon("School Management Icons/people_avatar.ico"))
        self.studentAdmission.setIconSize(QSize(120, 120))
        # self.studentAdmission.setFixedWidth(120)
        self.studentAdmission.clicked.connect(self.showStudentAdmission)
        self.studentAdmission.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow1.addWidget(self.studentAdmission)

        self.teachingStaff = QPushButton("Teaching\nStaff")
        self.teachingStaff.setFont(QFont("times new roman", 16))
        self.teachingStaff.setIcon(QIcon('School Management Icons/reading_university.ico'))
        self.teachingStaff.setIconSize(QSize(120, 120))
        # self.teachingStaff.setFixedWidth(120)
        self.teachingStaff.clicked.connect(self.showTeachingStaff)
        self.teachingStaff.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow1.addWidget(self.teachingStaff)

        self.NonteachingStaff = QPushButton("Non Teaching\nStaff")
        self.NonteachingStaff.setFont(QFont("times new roman", 16))
        # self.NonteachingStaff.setFixedWidth(180)
        self.NonteachingStaff.setIcon(QIcon('School Management Icons/workers.ico'))
        self.NonteachingStaff.setIconSize(QSize(120, 120))
        self.NonteachingStaff.clicked.connect(self.showNonTeachingStaff)
        self.NonteachingStaff.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:MediumPurple; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow1.addWidget(self.NonteachingStaff)

        self.marks = QPushButton("Marks")
        self.marks.setFont(QFont("times new roman", 16))
        # self.marks.setFixedWidth(120)
        self.marks.setIcon(QIcon('School Management Icons/result_school.ico'))
        self.marks.setIconSize(QSize(120, 120))
        self.marks.clicked.connect(self.showMarks)
        self.marks.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orange; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow1.addWidget(self.marks)

        self.vbox.addLayout(self.hboxRow1)


        self.StudentDailyAttendance = QPushButton("Student Daily\nAttendance")
        self.StudentDailyAttendance.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.StudentDailyAttendance.setIcon(QIcon('School Management Icons/schedule_calendar_checklist.ico'))
        self.StudentDailyAttendance.setIconSize(QSize(120, 120))
        self.StudentDailyAttendance.clicked.connect(self.showStudentAttendance)
        self.StudentDailyAttendance.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow1.addWidget(self.StudentDailyAttendance)


        self.hboxRow2 = QHBoxLayout()

        self.staffDailyAttendance = QPushButton("Staff Daily\nAttendance")
        self.staffDailyAttendance.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.staffDailyAttendance.setIcon(QIcon('School Management Icons/workers checklist.ico'))
        self.staffDailyAttendance.setIconSize(QSize(120, 120))
        self.staffDailyAttendance.clicked.connect(self.showStaffAttendance)
        self.staffDailyAttendance.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow2.addWidget(self.staffDailyAttendance)

        self.finances = QPushButton("Payment /\nFinances")
        self.finances.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.finances.setIcon(QIcon('School Management Icons/finance_analytics.ico'))
        self.finances.setIconSize(QSize(120, 120))
        self.finances.clicked.connect(self.showFinances)
        self.finances.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow2.addWidget(self.finances)

        self.classTimetable = QPushButton("Class\nTimetable")
        self.classTimetable.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.classTimetable.setIcon(QIcon('School Management Icons/calendar_clock.ico'))
        self.classTimetable.setIconSize(QSize(120, 120))
        self.classTimetable.clicked.connect(self.showClassTimetable)
        self.classTimetable.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow2.addWidget(self.classTimetable)

        self.thingsToDo = QPushButton("Things To Do")
        self.thingsToDo.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.thingsToDo.setIcon(QIcon('School Management Icons/wish_list.ico'))
        self.thingsToDo.setIconSize(QSize(120, 120))
        self.thingsToDo.clicked.connect(self.showThingsToDo)
        self.thingsToDo.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:magenta; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow2.addWidget(self.thingsToDo)

        self.others = QPushButton("Others")
        self.others.setFont(QFont("times new roman", 16))
        # self.StudentDailyAttendance.setFixedWidth(120)
        self.others.setIcon(QIcon('School Management Icons/abcMessage.ico'))
        self.others.setIconSize(QSize(120, 120))
        self.others.clicked.connect(self.showOthers)
        self.others.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:GreenYellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        self.hboxRow2.addWidget(self.others)

        self.vbox.addLayout(self.hboxRow2)

        self.label2 = QLabel()
        self.label2.setStyleSheet('background-color:white')
        self.label2.setFixedHeight(312)
        self.vbox.addWidget(self.label2)


        hbox2 = QHBoxLayout()

        hbox2.addWidget(self.btn_addp)
        # hbox2.addWidget(self.btn_removep)
        hbox2.addWidget(self.btn_minimize)
        hbox2.addWidget(self.btn_close)







        self.hbox = QHBoxLayout()

        self.btn9212 = QPushButton()
        self.btn9212.setFixedWidth(63)
        self.btn9212.setIcon(QIcon('School Management Icons/university_library.ico'))
        self.btn9212.setIconSize(QSize(60, 60))
        self.btn9212.clicked.connect(self.panel)
        self.vbox_side.addWidget(self.btn9212)

        # self.vbox_side.setAlignment(Qt.AlignTop)
        self.vbox_side.addItem(self.vbox_side_content)
        self.hbox.addLayout(self.vbox_side)
        self.vbox.addLayout(hbox2)
        self.hbox.addItem(self.vbox)

        self.vboxMain.addLayout(self.hbox)

        self.setLayout(self.vboxMain)

    def check(self):
        global permission
        if permission == False:
            self.closew()
        elif permission == True:
            return


# function that is called when a new entry is chosen from the first dropdown list

    def removeDashboard(self):
        self.studentAdmission.hide()
        self.teachingStaff.hide()
        self.NonteachingStaff.hide()
        self.marks.hide()
        self.StudentDailyAttendance.hide()
        self.staffDailyAttendance.hide()
        self.finances.hide()
        self.classTimetable.hide()
        self.thingsToDo.hide()
        self.others.hide()
        self.label2.hide()

    def showDashboard(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

    def showStudentAdmission(self):
        print('correctly called the admission function')
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()

        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Student Admission")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Student Admission")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("Sanserif", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.hboxRow12 = QHBoxLayout()
            self.hboxRow13 = QHBoxLayout()
            self.hboxRow3 = QHBoxLayout()
            self.hboxRow4 = QHBoxLayout()

            self.label_StudentName = QLabel("Student Name")
            self.label_StudentName.setAlignment(Qt.AlignCenter)
            self.label_StudentName.setFont(QFont("times new roman", 12))
            self.label_StudentName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentName)
            # self.label_StudentName.hide()

            self.label_StudentNR = QLabel("Student Nr / ID")
            self.label_StudentNR.setAlignment(Qt.AlignCenter)
            self.label_StudentNR.setFont(QFont("times new roman", 12))
            self.label_StudentNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orange; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentNR)
            # self.label_StudentNR.hide()

            self.label_Category = QLabel("Category")
            self.label_Category.setAlignment(Qt.AlignCenter)
            self.label_Category.setFont(QFont("times new roman", 12))
            self.label_Category.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightcyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_Category)

            self.vbox2.addLayout(self.hboxRow12)

            self.line_edit_StudentName = QLineEdit()
            self.line_edit_StudentName.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentName.setFont(QFont("times new roman", 12))
            self.line_edit_StudentName.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentName)
            # self.line_edit_StudentName.hide()

            self.line_edit_StudentNR = QLineEdit()
            self.line_edit_StudentNR.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentNR.setFont(QFont("times new roman", 12))
            self.line_edit_StudentNR.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentNR)
            # self.line_edit_StudentNR.hide()

            self.Category_cbox = QComboBox()
            # self.Gender_cbox.setAlignment(Qt.AlignCenter)
            self.Category_cbox.setFont(QFont("times new roman", 16))
            self.Category_cbox.setFixedWidth(420)
            # self.Gender_cbox.setStyleSheet("background-color:white")
            self.Category_cbox.addItem("Child")
            self.Category_cbox.addItem("Teenager")
            self.Category_cbox.addItem("Adult")
            self.hboxRow13.addWidget(self.Category_cbox)

            self.vbox2.addLayout(self.hboxRow13)

            # new

            self.hboxRow15 = QHBoxLayout()

            self.label_Gender = QLabel("Gender")
            self.label_Gender.setAlignment(Qt.AlignCenter)
            self.label_Gender.setFont(QFont("times new roman", 12))
            self.label_Gender.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:salmon; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Gender)
            # self.label_StudentName.hide()

            self.label_DOB = QLabel("Date Of Birth")
            self.label_DOB.setAlignment(Qt.AlignCenter)
            self.label_DOB.setFont(QFont("times new roman", 12))
            self.label_DOB.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:tomato; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_DOB)
            # self.label_StudentNR.hide()

            self.label_Telephone = QLabel("Telephone")
            self.label_Telephone.setAlignment(Qt.AlignCenter)
            self.label_Telephone.setFont(QFont("times new roman", 12))
            self.label_Telephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Telephone)

            self.vbox2.addLayout(self.hboxRow15)

            self.hboxRow16 = QHBoxLayout()

            self.Gender_cbox = QComboBox()
            # self.Gender_cbox.setAlignment(Qt.AlignCenter)
            self.Gender_cbox.setFont(QFont("times new roman", 16))
            # self.Gender_cbox.setStyleSheet("background-color:white")
            self.Gender_cbox.addItem("Male")
            self.Gender_cbox.addItem("Female")
            self.Gender_cbox.addItem("Other")
            self.hboxRow16.addWidget(self.Gender_cbox)
            # self.line_edit_StudentName.hide()

            self.DateOfBirth = QDateEdit(calendarPopup=True)
            self.DateOfBirth.setDateTime(QDateTime.currentDateTime())
            self.DateOfBirth.setAlignment(Qt.AlignCenter)
            self.DateOfBirth.setFont(QFont("times new roman", 16))
            # self.DateOfBirth.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.DateOfBirth)
            # self.line_edit_StudentNR.hide()

            self.line_edit_Telephone = QLineEdit()
            self.line_edit_Telephone.setAlignment(Qt.AlignCenter)
            self.line_edit_Telephone.setFixedWidth(420)
            self.line_edit_Telephone.setFont(QFont("times new roman", 12))
            self.line_edit_Telephone.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.line_edit_Telephone)

            self.vbox2.addLayout(self.hboxRow16)

            self.label_FathersName = QLabel("Fathers Name")
            self.label_FathersName.setAlignment(Qt.AlignCenter)
            self.label_FathersName.setFont(QFont("times new roman", 12))
            self.label_FathersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersName)
            # self.label_FathersName.hide()

            self.label_FathersNR = QLabel("Fathers Mobile")
            self.label_FathersNR.setAlignment(Qt.AlignCenter)
            self.label_FathersNR.setFont(QFont("times new roman", 12))
            self.label_FathersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:springgreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersNR)
            # self.label_StudentNR.hide()

            self.label_FathersEmail = QLabel("Fathers Email")
            self.label_FathersEmail.setAlignment(Qt.AlignCenter)
            self.label_FathersEmail.setFont(QFont("times new roman", 12))
            self.label_FathersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersEmail)

            self.vbox2.addLayout(self.hboxRow3)

            self.line_edit_FathersName = QLineEdit()
            self.line_edit_FathersName.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersName.setFont(QFont("times new roman", 12))
            self.line_edit_FathersName.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_FathersNR = QLineEdit()
            self.line_edit_FathersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersNR.setFont(QFont("times new roman", 12))
            self.line_edit_FathersNR.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_FathersEmail = QLineEdit()
            self.line_edit_FathersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_FathersEmail.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersEmail)

            self.vbox2.addLayout(self.hboxRow4)

            self.hboxRow5 = QHBoxLayout()
            self.hboxRow6 = QHBoxLayout()

            self.label_MothersName = QLabel("Mothers Name")
            self.label_MothersName.setAlignment(Qt.AlignCenter)
            self.label_MothersName.setFont(QFont("times new roman", 12))
            self.label_MothersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersName)
            # self.label_FathersName.hide()

            self.label_MothersNR = QLabel("Mothers Mobile")
            self.label_MothersNR.setAlignment(Qt.AlignCenter)
            self.label_MothersNR.setFont(QFont("times new roman", 12))
            self.label_MothersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:MediumPurple; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersNR)
            # self.label_StudentNR.hide()

            self.label_MothersEmail = QLabel("Mothers Email")
            self.label_MothersEmail.setAlignment(Qt.AlignCenter)
            self.label_MothersEmail.setFont(QFont("times new roman", 12))
            self.label_MothersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersEmail)

            self.vbox2.addLayout(self.hboxRow5)

            self.line_edit_MothersName = QLineEdit()
            self.line_edit_MothersName.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersName.setFont(QFont("times new roman", 12))
            self.line_edit_MothersName.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_MothersNR = QLineEdit()
            self.line_edit_MothersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersNR.setFont(QFont("times new roman", 12))
            self.line_edit_MothersNR.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_MothersEmail = QLineEdit()
            self.line_edit_MothersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_MothersEmail.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersEmail)

            self.vbox2.addLayout(self.hboxRow6)

            self.hboxRow7 = QHBoxLayout()

            self.address_label = QLabel("  Address  ")
            self.address_label.setAlignment(Qt.AlignCenter)
            self.address_label.setFont(QFont("times new roman", 12))
            self.address_label.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:magenta; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow7.addWidget(self.address_label)

            self.address_text = QTextEdit()
            self.address_text.setAlignment(Qt.AlignCenter)
            self.address_text.setFont(QFont("times new roman", 12))
            self.address_text.setStyleSheet("background-color:white")
            self.hboxRow7.addWidget(self.address_text)

            self.vbox2.addLayout(self.hboxRow7)

            self.hboxRow8 = QHBoxLayout()
            self.hboxRow9 = QHBoxLayout()

            self.label_PostCode = QLabel("Post Code")
            self.label_PostCode.setAlignment(Qt.AlignCenter)
            self.label_PostCode.setFont(QFont("times new roman", 12))
            self.label_PostCode.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_PostCode)
            # self.label_FathersName.hide()

            self.label_Email = QLabel("Email")
            self.label_Email.setAlignment(Qt.AlignCenter)
            self.label_Email.setFont(QFont("times new roman", 12))
            self.label_Email.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_Email)

            self.label_shift = QLabel("Shift")
            self.label_shift.setAlignment(Qt.AlignCenter)
            self.label_shift.setFont(QFont("times new roman", 12))
            self.label_shift.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_shift)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow8)

            self.line_edit_PostCode = QLineEdit()
            self.line_edit_PostCode.setAlignment(Qt.AlignCenter)
            self.line_edit_PostCode.setFont(QFont("times new roman", 12))
            self.line_edit_PostCode.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_PostCode)
            # self.line_edit_FathersName.hide()

            self.line_edit_Email = QLineEdit()
            self.line_edit_Email.setAlignment(Qt.AlignCenter)
            self.line_edit_Email.setFont(QFont("times new roman", 12))
            self.line_edit_Email.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_Email)

            self.Shift_list = QComboBox()
            # self.Shift_list.setAlignment(Qt.AlignCenter)
            self.Shift_list.setFont(QFont("times new roman", 12))
            self.Shift_list.setFixedWidth(420)
            # self.Shift_list.setStyleSheet("background-color:white")
            fhand = open('shifts.txt', 'r')
            for line in fhand:
                if len(line.strip()) > 0:
                    self.Shift_list.addItem(line.strip())

            self.hboxRow9.addWidget(self.Shift_list)
            # self.line_edit_FathersNR.hide()

            self.vbox2.addLayout(self.hboxRow9)

            self.hboxRow17 = QHBoxLayout()
            self.hboxRow18 = QHBoxLayout()

            self.label_GPName = QLabel("G.P's Name (Medical Info)")
            self.label_GPName.setAlignment(Qt.AlignCenter)
            self.label_GPName.setFont(QFont("times new roman", 12))
            self.label_GPName.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:deepskyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPName)
            # self.label_FathersName.hide()

            self.label_GPTelephone = QLabel("G.P's Telephone (Medical Info)")
            self.label_GPTelephone.setAlignment(Qt.AlignCenter)
            self.label_GPTelephone.setFont(QFont("times new roman", 12))
            self.label_GPTelephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mediumorchid; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPTelephone)

            self.label_Class = QLabel("Class")
            self.label_Class.setAlignment(Qt.AlignCenter)
            self.label_Class.setFont(QFont("times new roman", 12))
            self.label_Class.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mistyrose; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_Class)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow17)

            self.line_edit_GPName = QLineEdit()
            self.line_edit_GPName.setAlignment(Qt.AlignCenter)
            self.line_edit_GPName.setFont(QFont("times new roman", 12))
            self.line_edit_GPName.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPName)
            # self.line_edit_FathersName.hide()

            self.line_edit_GPTelephone = QLineEdit()
            self.line_edit_GPTelephone.setAlignment(Qt.AlignCenter)
            self.line_edit_GPTelephone.setFont(QFont("times new roman", 12))
            self.line_edit_GPTelephone.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPTelephone)

            self.line_edit_Class = QComboBox()
            self.line_edit_Class.setFont(QFont("times new roman", 12))
            self.line_edit_Class.setFixedWidth(420)
            fhand = open('Classes.txt', 'r')
            for line in fhand:
                if len(line.strip()) > 0:
                    self.line_edit_Class.addItem(line.strip())
            self.hboxRow18.addWidget(self.line_edit_Class)

            self.vbox2.addLayout(self.hboxRow18)



            self.hboxRow10 = QHBoxLayout()

            self.comments_student = QTextEdit()
            self.comments_student.setAlignment(Qt.AlignCenter)
            self.comments_student.setPlaceholderText('Comments about Student')
            self.comments_student.setFont(QFont("times new roman", 12))
            self.comments_student.setStyleSheet("background-color:white")
            self.hboxRow10.addWidget(self.comments_student)

            self.submit_student = QPushButton('S\nU\nB\nM\nI\nT')
            self.submit_student.setStyleSheet("font-family:times new roman; font-size: 16px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.submit_student.clicked.connect(self.newStudent)
            self.hboxRow10.addWidget(self.submit_student)

            self.vbox2.addLayout(self.hboxRow10)


            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def addNewTeacher(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()

        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Teacher Registration")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Teacher Registration")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.hboxRow12 = QHBoxLayout()
            self.hboxRow13 = QHBoxLayout()
            self.hboxRow3 = QHBoxLayout()
            self.hboxRow4 = QHBoxLayout()

            self.label_StudentName = QLabel("Name")
            self.label_StudentName.setAlignment(Qt.AlignCenter)
            self.label_StudentName.setFont(QFont("times new roman", 12))
            self.label_StudentName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentName)
            # self.label_StudentName.hide()

            self.label_StudentNR = QLabel("ID")
            self.label_StudentNR.setAlignment(Qt.AlignCenter)
            self.label_StudentNR.setFont(QFont("times new roman", 12))
            self.label_StudentNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orange; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentNR)
            # self.label_StudentNR.hide()

            self.label_mobile = QLabel("Mobile #")
            self.label_mobile.setAlignment(Qt.AlignCenter)
            self.label_mobile.setFont(QFont("times new roman", 12))
            self.label_mobile.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightcyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_mobile)

            self.vbox2.addLayout(self.hboxRow12)

            self.line_edit_StudentName = QLineEdit()
            self.line_edit_StudentName.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentName.setFont(QFont("times new roman", 12))
            self.line_edit_StudentName.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentName)
            # self.line_edit_StudentName.hide()

            self.line_edit_StudentNR = QLineEdit()
            self.line_edit_StudentNR.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentNR.setFont(QFont("times new roman", 12))
            self.line_edit_StudentNR.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentNR)
            # self.line_edit_StudentNR.hide()

            self.line_edit_mobile = QLineEdit()
            self.line_edit_mobile.setAlignment(Qt.AlignCenter)
            self.line_edit_mobile.setFont(QFont("times new roman", 12))
            self.line_edit_mobile.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_mobile)

            self.vbox2.addLayout(self.hboxRow13)

            self.hboxRow15 = QHBoxLayout()

            self.label_Gender = QLabel("Gender")
            self.label_Gender.setAlignment(Qt.AlignCenter)
            self.label_Gender.setFont(QFont("times new roman", 12))
            self.label_Gender.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:salmon; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Gender)
            # self.label_StudentName.hide()

            self.label_DOB = QLabel("Date Of Birth")
            self.label_DOB.setAlignment(Qt.AlignCenter)
            self.label_DOB.setFont(QFont("times new roman", 12))
            self.label_DOB.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:tomato; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_DOB)
            # self.label_StudentNR.hide()

            self.label_Telephone = QLabel("Telephone")
            self.label_Telephone.setAlignment(Qt.AlignCenter)
            self.label_Telephone.setFont(QFont("times new roman", 12))
            self.label_Telephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Telephone)

            self.vbox2.addLayout(self.hboxRow15)

            self.hboxRow16 = QHBoxLayout()

            self.Gender_cbox = QComboBox()
            # self.Gender_cbox.setAlignment(Qt.AlignCenter)
            self.Gender_cbox.setFont(QFont("times new roman", 16))
            # self.Gender_cbox.setStyleSheet("background-color:white")
            self.Gender_cbox.addItem("Male")
            self.Gender_cbox.addItem("Female")
            self.Gender_cbox.addItem("Other")
            self.hboxRow16.addWidget(self.Gender_cbox)
            # self.line_edit_StudentName.hide()

            self.DateOfBirth = QDateEdit(calendarPopup=True)
            self.DateOfBirth.setDateTime(QDateTime.currentDateTime())
            self.DateOfBirth.setAlignment(Qt.AlignCenter)
            self.DateOfBirth.setFont(QFont("times new roman", 16))
            # self.DateOfBirth.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.DateOfBirth)
            # self.line_edit_StudentNR.hide()

            self.line_edit_Telephone = QLineEdit()
            self.line_edit_Telephone.setAlignment(Qt.AlignCenter)
            self.line_edit_Telephone.setFixedWidth(420)
            self.line_edit_Telephone.setFont(QFont("times new roman", 12))
            self.line_edit_Telephone.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.line_edit_Telephone)

            self.vbox2.addLayout(self.hboxRow16)

            self.label_FathersName = QLabel("Fathers Name")
            self.label_FathersName.setAlignment(Qt.AlignCenter)
            self.label_FathersName.setFont(QFont("times new roman", 12))
            self.label_FathersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersName)
            # self.label_FathersName.hide()

            self.label_FathersNR = QLabel("Fathers Mobile")
            self.label_FathersNR.setAlignment(Qt.AlignCenter)
            self.label_FathersNR.setFont(QFont("times new roman", 12))
            self.label_FathersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:springgreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersNR)
            # self.label_StudentNR.hide()

            self.label_FathersEmail = QLabel("Fathers Email")
            self.label_FathersEmail.setAlignment(Qt.AlignCenter)
            self.label_FathersEmail.setFont(QFont("times new roman", 12))
            self.label_FathersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersEmail)

            self.vbox2.addLayout(self.hboxRow3)

            self.line_edit_FathersName = QLineEdit()
            self.line_edit_FathersName.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersName.setFont(QFont("times new roman", 12))
            self.line_edit_FathersName.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_FathersNR = QLineEdit()
            self.line_edit_FathersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersNR.setFont(QFont("times new roman", 12))
            self.line_edit_FathersNR.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_FathersEmail = QLineEdit()
            self.line_edit_FathersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_FathersEmail.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersEmail)

            self.vbox2.addLayout(self.hboxRow4)

            self.hboxRow5 = QHBoxLayout()
            self.hboxRow6 = QHBoxLayout()

            self.label_MothersName = QLabel("Next of Kin : Name")
            self.label_MothersName.setAlignment(Qt.AlignCenter)
            self.label_MothersName.setFont(QFont("times new roman", 12))
            self.label_MothersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersName)
            # self.label_FathersName.hide()

            self.label_MothersNR = QLabel("Next of Kin : Mobile")
            self.label_MothersNR.setAlignment(Qt.AlignCenter)
            self.label_MothersNR.setFont(QFont("times new roman", 12))
            self.label_MothersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:MediumPurple; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersNR)
            # self.label_StudentNR.hide()

            self.label_MothersEmail = QLabel("Next of Kin : Email")
            self.label_MothersEmail.setAlignment(Qt.AlignCenter)
            self.label_MothersEmail.setFont(QFont("times new roman", 12))
            self.label_MothersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersEmail)

            self.vbox2.addLayout(self.hboxRow5)

            self.line_edit_MothersName = QLineEdit()
            self.line_edit_MothersName.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersName.setFont(QFont("times new roman", 12))
            self.line_edit_MothersName.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_MothersNR = QLineEdit()
            self.line_edit_MothersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersNR.setFont(QFont("times new roman", 12))
            self.line_edit_MothersNR.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_MothersEmail = QLineEdit()
            self.line_edit_MothersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_MothersEmail.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersEmail)

            self.vbox2.addLayout(self.hboxRow6)

            self.hboxRow7 = QHBoxLayout()

            self.address_label = QLabel("  Address  ")
            self.address_label.setAlignment(Qt.AlignCenter)
            self.address_label.setFont(QFont("times new roman", 12))
            self.address_label.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:magenta; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow7.addWidget(self.address_label)

            self.address_text = QTextEdit()
            self.address_text.setAlignment(Qt.AlignCenter)
            self.address_text.setFont(QFont("times new roman", 12))
            self.address_text.setStyleSheet("background-color:white")
            self.hboxRow7.addWidget(self.address_text)

            self.vbox2.addLayout(self.hboxRow7)

            self.hboxRow8 = QHBoxLayout()
            self.hboxRow9 = QHBoxLayout()

            self.label_PostCode = QLabel("Post Code")
            self.label_PostCode.setAlignment(Qt.AlignCenter)
            self.label_PostCode.setFont(QFont("times new roman", 12))
            self.label_PostCode.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_PostCode)
            # self.label_FathersName.hide()

            self.label_Email = QLabel("Email")
            self.label_Email.setAlignment(Qt.AlignCenter)
            self.label_Email.setFont(QFont("times new roman", 12))
            self.label_Email.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_Email)

            self.label_shift = QLabel("Shift")
            self.label_shift.setAlignment(Qt.AlignCenter)
            self.label_shift.setFont(QFont("times new roman", 12))
            self.label_shift.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_shift)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow8)

            self.line_edit_PostCode = QLineEdit()
            self.line_edit_PostCode.setAlignment(Qt.AlignCenter)
            self.line_edit_PostCode.setFont(QFont("times new roman", 12))
            self.line_edit_PostCode.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_PostCode)
            # self.line_edit_FathersName.hide()

            self.line_edit_Email = QLineEdit()
            self.line_edit_Email.setAlignment(Qt.AlignCenter)
            self.line_edit_Email.setFont(QFont("times new roman", 12))
            self.line_edit_Email.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_Email)

            self.line_edit_Shift = QLineEdit()
            self.line_edit_Shift.setAlignment(Qt.AlignCenter)
            self.line_edit_Shift.setFont(QFont("times new roman", 12))
            self.line_edit_Shift.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_Shift)
            # self.line_edit_FathersNR.hide()

            self.vbox2.addLayout(self.hboxRow9)

            self.hboxRow17 = QHBoxLayout()
            self.hboxRow18 = QHBoxLayout()

            self.label_GPName = QLabel("G.P's Name (Medical Info)")
            self.label_GPName.setAlignment(Qt.AlignCenter)
            self.label_GPName.setFont(QFont("times new roman", 12))
            self.label_GPName.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:deepskyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPName)
            # self.label_FathersName.hide()

            self.label_GPTelephone = QLabel("G.P's Telephone (Medical Info)")
            self.label_GPTelephone.setAlignment(Qt.AlignCenter)
            self.label_GPTelephone.setFont(QFont("times new roman", 12))
            self.label_GPTelephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mediumorchid; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPTelephone)

            self.label_Designation = QLabel("Designation")
            self.label_Designation.setAlignment(Qt.AlignCenter)
            self.label_Designation.setFont(QFont("times new roman", 12))
            self.label_Designation.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mistyrose; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_Designation)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow17)

            self.line_edit_GPName = QLineEdit()
            self.line_edit_GPName.setAlignment(Qt.AlignCenter)
            self.line_edit_GPName.setFont(QFont("times new roman", 12))
            self.line_edit_GPName.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPName)
            # self.line_edit_FathersName.hide()

            self.line_edit_GPTelephone = QLineEdit()
            self.line_edit_GPTelephone.setAlignment(Qt.AlignCenter)
            self.line_edit_GPTelephone.setFont(QFont("times new roman", 12))
            self.line_edit_GPTelephone.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPTelephone)

            self.line_edit_Designation = QLineEdit()
            self.line_edit_Designation.setAlignment(Qt.AlignCenter)
            self.line_edit_Designation.setFont(QFont("times new roman", 12))
            self.line_edit_Designation.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_Designation)

            self.vbox2.addLayout(self.hboxRow18)

            self.hboxRow10 = QHBoxLayout()

            self.comments_student = QTextEdit()
            self.comments_student.setAlignment(Qt.AlignCenter)
            self.comments_student.setPlaceholderText('Description / Resume / Comments')
            self.comments_student.setFont(QFont("times new roman", 12))
            self.comments_student.setStyleSheet("background-color:white")
            self.hboxRow10.addWidget(self.comments_student)

            self.submit_student = QPushButton('S\nU\nB\nM\nI\nT')
            self.submit_student.setStyleSheet("font-family:times new roman; font-size: 16px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.submit_student.clicked.connect(self.newTeacher)
            self.hboxRow10.addWidget(self.submit_student)

            self.vbox2.addLayout(self.hboxRow10)


            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def addNewStaff(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()

        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Staff Registration")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Staff Registration")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.hboxRow12 = QHBoxLayout()
            self.hboxRow13 = QHBoxLayout()
            self.hboxRow3 = QHBoxLayout()
            self.hboxRow4 = QHBoxLayout()

            self.label_StudentName = QLabel("Name")
            self.label_StudentName.setAlignment(Qt.AlignCenter)
            self.label_StudentName.setFont(QFont("times new roman", 12))
            self.label_StudentName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentName)
            # self.label_StudentName.hide()

            self.label_StudentNR = QLabel("ID")
            self.label_StudentNR.setAlignment(Qt.AlignCenter)
            self.label_StudentNR.setFont(QFont("times new roman", 12))
            self.label_StudentNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orange; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_StudentNR)
            # self.label_StudentNR.hide()

            self.label_mobile = QLabel("Mobile #")
            self.label_mobile.setAlignment(Qt.AlignCenter)
            self.label_mobile.setFont(QFont("times new roman", 12))
            self.label_mobile.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightcyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow12.addWidget(self.label_mobile)

            self.vbox2.addLayout(self.hboxRow12)

            self.line_edit_StudentName = QLineEdit()
            self.line_edit_StudentName.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentName.setFont(QFont("times new roman", 12))
            self.line_edit_StudentName.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentName)
            # self.line_edit_StudentName.hide()

            self.line_edit_StudentNR = QLineEdit()
            self.line_edit_StudentNR.setAlignment(Qt.AlignCenter)
            self.line_edit_StudentNR.setFont(QFont("times new roman", 12))
            self.line_edit_StudentNR.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_StudentNR)
            # self.line_edit_StudentNR.hide()

            self.line_edit_mobile = QLineEdit()
            self.line_edit_mobile.setAlignment(Qt.AlignCenter)
            self.line_edit_mobile.setFont(QFont("times new roman", 12))
            self.line_edit_mobile.setStyleSheet("background-color:white")
            self.hboxRow13.addWidget(self.line_edit_mobile)

            self.vbox2.addLayout(self.hboxRow13)

            self.hboxRow15 = QHBoxLayout()

            self.label_Gender = QLabel("Gender")
            self.label_Gender.setAlignment(Qt.AlignCenter)
            self.label_Gender.setFont(QFont("times new roman", 12))
            self.label_Gender.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:salmon; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Gender)
            # self.label_StudentName.hide()

            self.label_DOB = QLabel("Date Of Birth")
            self.label_DOB.setAlignment(Qt.AlignCenter)
            self.label_DOB.setFont(QFont("times new roman", 12))
            self.label_DOB.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:tomato; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_DOB)
            # self.label_StudentNR.hide()

            self.label_Telephone = QLabel("Telephone")
            self.label_Telephone.setAlignment(Qt.AlignCenter)
            self.label_Telephone.setFont(QFont("times new roman", 12))
            self.label_Telephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow15.addWidget(self.label_Telephone)

            self.vbox2.addLayout(self.hboxRow15)

            self.hboxRow16 = QHBoxLayout()

            self.Gender_cbox = QComboBox()
            # self.Gender_cbox.setAlignment(Qt.AlignCenter)
            self.Gender_cbox.setFont(QFont("times new roman", 16))
            # self.Gender_cbox.setStyleSheet("background-color:white")
            self.Gender_cbox.addItem("Male")
            self.Gender_cbox.addItem("Female")
            self.Gender_cbox.addItem("Other")
            self.hboxRow16.addWidget(self.Gender_cbox)
            # self.line_edit_StudentName.hide()

            self.DateOfBirth = QDateEdit(calendarPopup=True)
            self.DateOfBirth.setDateTime(QDateTime.currentDateTime())
            self.DateOfBirth.setAlignment(Qt.AlignCenter)
            self.DateOfBirth.setFont(QFont("times new roman", 16))
            # self.DateOfBirth.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.DateOfBirth)
            # self.line_edit_StudentNR.hide()

            self.line_edit_Telephone = QLineEdit()
            self.line_edit_Telephone.setAlignment(Qt.AlignCenter)
            self.line_edit_Telephone.setFixedWidth(420)
            self.line_edit_Telephone.setFont(QFont("times new roman", 12))
            self.line_edit_Telephone.setStyleSheet("background-color:white")
            self.hboxRow16.addWidget(self.line_edit_Telephone)

            self.vbox2.addLayout(self.hboxRow16)

            self.label_FathersName = QLabel("Fathers Name")
            self.label_FathersName.setAlignment(Qt.AlignCenter)
            self.label_FathersName.setFont(QFont("times new roman", 12))
            self.label_FathersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersName)
            # self.label_FathersName.hide()

            self.label_FathersNR = QLabel("Fathers Mobile")
            self.label_FathersNR.setAlignment(Qt.AlignCenter)
            self.label_FathersNR.setFont(QFont("times new roman", 12))
            self.label_FathersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:springgreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersNR)
            # self.label_StudentNR.hide()

            self.label_FathersEmail = QLabel("Fathers Email")
            self.label_FathersEmail.setAlignment(Qt.AlignCenter)
            self.label_FathersEmail.setFont(QFont("times new roman", 12))
            self.label_FathersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow3.addWidget(self.label_FathersEmail)

            self.vbox2.addLayout(self.hboxRow3)

            self.line_edit_FathersName = QLineEdit()
            self.line_edit_FathersName.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersName.setFont(QFont("times new roman", 12))
            self.line_edit_FathersName.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_FathersNR = QLineEdit()
            self.line_edit_FathersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersNR.setFont(QFont("times new roman", 12))
            self.line_edit_FathersNR.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_FathersEmail = QLineEdit()
            self.line_edit_FathersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_FathersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_FathersEmail.setStyleSheet("background-color:white")
            self.hboxRow4.addWidget(self.line_edit_FathersEmail)

            self.vbox2.addLayout(self.hboxRow4)

            self.hboxRow5 = QHBoxLayout()
            self.hboxRow6 = QHBoxLayout()

            self.label_MothersName = QLabel("Next of Kin : Name")
            self.label_MothersName.setAlignment(Qt.AlignCenter)
            self.label_MothersName.setFont(QFont("times new roman", 12))
            self.label_MothersName.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersName)
            # self.label_FathersName.hide()

            self.label_MothersNR = QLabel("Next of Kin : Mobile")
            self.label_MothersNR.setAlignment(Qt.AlignCenter)
            self.label_MothersNR.setFont(QFont("times new roman", 12))
            self.label_MothersNR.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:MediumPurple; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersNR)
            # self.label_StudentNR.hide()

            self.label_MothersEmail = QLabel("Next of Kin : Email")
            self.label_MothersEmail.setAlignment(Qt.AlignCenter)
            self.label_MothersEmail.setFont(QFont("times new roman", 12))
            self.label_MothersEmail.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow5.addWidget(self.label_MothersEmail)

            self.vbox2.addLayout(self.hboxRow5)

            self.line_edit_MothersName = QLineEdit()
            self.line_edit_MothersName.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersName.setFont(QFont("times new roman", 12))
            self.line_edit_MothersName.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersName)
            # self.line_edit_FathersName.hide()

            self.line_edit_MothersNR = QLineEdit()
            self.line_edit_MothersNR.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersNR.setFont(QFont("times new roman", 12))
            self.line_edit_MothersNR.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersNR)
            # self.line_edit_FathersNR.hide()

            self.line_edit_MothersEmail = QLineEdit()
            self.line_edit_MothersEmail.setAlignment(Qt.AlignCenter)
            self.line_edit_MothersEmail.setFont(QFont("times new roman", 12))
            self.line_edit_MothersEmail.setStyleSheet("background-color:white")
            self.hboxRow6.addWidget(self.line_edit_MothersEmail)

            self.vbox2.addLayout(self.hboxRow6)

            self.hboxRow7 = QHBoxLayout()

            self.address_label = QLabel("  Address  ")
            self.address_label.setAlignment(Qt.AlignCenter)
            self.address_label.setFont(QFont("times new roman", 12))
            self.address_label.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:magenta; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow7.addWidget(self.address_label)

            self.address_text = QTextEdit()
            self.address_text.setAlignment(Qt.AlignCenter)
            self.address_text.setFont(QFont("times new roman", 12))
            self.address_text.setStyleSheet("background-color:white")
            self.hboxRow7.addWidget(self.address_text)

            self.vbox2.addLayout(self.hboxRow7)

            self.hboxRow8 = QHBoxLayout()
            self.hboxRow9 = QHBoxLayout()

            self.label_PostCode = QLabel("Post Code")
            self.label_PostCode.setAlignment(Qt.AlignCenter)
            self.label_PostCode.setFont(QFont("times new roman", 12))
            self.label_PostCode.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_PostCode)
            # self.label_FathersName.hide()

            self.label_Email = QLabel("Email")
            self.label_Email.setAlignment(Qt.AlignCenter)
            self.label_Email.setFont(QFont("times new roman", 12))
            self.label_Email.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_Email)

            self.label_shift = QLabel("Shift")
            self.label_shift.setAlignment(Qt.AlignCenter)
            self.label_shift.setFont(QFont("times new roman", 12))
            self.label_shift.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow8.addWidget(self.label_shift)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow8)

            self.line_edit_PostCode = QLineEdit()
            self.line_edit_PostCode.setAlignment(Qt.AlignCenter)
            self.line_edit_PostCode.setFont(QFont("times new roman", 12))
            self.line_edit_PostCode.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_PostCode)
            # self.line_edit_FathersName.hide()

            self.line_edit_Email = QLineEdit()
            self.line_edit_Email.setAlignment(Qt.AlignCenter)
            self.line_edit_Email.setFont(QFont("times new roman", 12))
            self.line_edit_Email.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_Email)

            self.line_edit_Shift = QLineEdit()
            self.line_edit_Shift.setAlignment(Qt.AlignCenter)
            self.line_edit_Shift.setFont(QFont("times new roman", 12))
            self.line_edit_Shift.setStyleSheet("background-color:white")
            self.hboxRow9.addWidget(self.line_edit_Shift)
            # self.line_edit_FathersNR.hide()

            self.vbox2.addLayout(self.hboxRow9)

            self.hboxRow17 = QHBoxLayout()
            self.hboxRow18 = QHBoxLayout()

            self.label_GPName = QLabel("G.P's Name (Medical Info)")
            self.label_GPName.setAlignment(Qt.AlignCenter)
            self.label_GPName.setFont(QFont("times new roman", 12))
            self.label_GPName.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:deepskyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPName)
            # self.label_FathersName.hide()

            self.label_GPTelephone = QLabel("G.P's Telephone (Medical Info)")
            self.label_GPTelephone.setAlignment(Qt.AlignCenter)
            self.label_GPTelephone.setFont(QFont("times new roman", 12))
            self.label_GPTelephone.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mediumorchid; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_GPTelephone)

            self.label_Designation = QLabel("Designation")
            self.label_Designation.setAlignment(Qt.AlignCenter)
            self.label_Designation.setFont(QFont("times new roman", 12))
            self.label_Designation.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:mistyrose; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.hboxRow17.addWidget(self.label_Designation)
            # self.label_StudentNR.hide()

            self.vbox2.addLayout(self.hboxRow17)

            self.line_edit_GPName = QLineEdit()
            self.line_edit_GPName.setAlignment(Qt.AlignCenter)
            self.line_edit_GPName.setFont(QFont("times new roman", 12))
            self.line_edit_GPName.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPName)
            # self.line_edit_FathersName.hide()

            self.line_edit_GPTelephone = QLineEdit()
            self.line_edit_GPTelephone.setAlignment(Qt.AlignCenter)
            self.line_edit_GPTelephone.setFont(QFont("times new roman", 12))
            self.line_edit_GPTelephone.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_GPTelephone)

            self.line_edit_Designation = QLineEdit()
            self.line_edit_Designation.setAlignment(Qt.AlignCenter)
            self.line_edit_Designation.setFont(QFont("times new roman", 12))
            self.line_edit_Designation.setStyleSheet("background-color:white")
            self.hboxRow18.addWidget(self.line_edit_Designation)

            self.vbox2.addLayout(self.hboxRow18)

            self.hboxRow10 = QHBoxLayout()

            self.comments_student = QTextEdit()
            self.comments_student.setAlignment(Qt.AlignCenter)
            self.comments_student.setPlaceholderText('Description / Resume / Comments')
            self.comments_student.setFont(QFont("times new roman", 12))
            self.comments_student.setStyleSheet("background-color:white")
            self.hboxRow10.addWidget(self.comments_student)

            self.submit_student = QPushButton('S\nU\nB\nM\nI\nT')
            self.submit_student.setStyleSheet("font-family:times new roman; font-size: 16px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.submit_student.clicked.connect(self.newStaff)
            self.hboxRow10.addWidget(self.submit_student)

            self.vbox2.addLayout(self.hboxRow10)


            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")


    def showStudentAttendance(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Students Daily Attendance")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Students Daily Attendance")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.hboxRow14 = QHBoxLayout()

            self.totalstudents = QLabel(f'\t\tTotal Students : {12}\t\tMale : {7}\t\tFemale : {5}\t\t')
            self.totalstudents.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
            self.hboxRow14.addWidget(self.totalstudents)

            self.addTeacher = QPushButton('ATTENDANCE By CLASS')
            self.addTeacher.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.addTeacher.clicked.connect(self.addAttendance)
            self.hboxRow14.addWidget(self.addTeacher)

            self.vbox2.addLayout(self.hboxRow14)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()
            self.getStudentsAttendance()

            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def getStudentsAttendance(self):
        global maleTeacher
        global femaleTeacher
        maleTeacher = 0
        femaleTeacher = 0
        path = 'Students Attendance' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print(mydata)
            if mydata.iloc[11][1] == 'Male':
                maleTeacher += 1
            elif mydata.iloc[11][1] == 'Female':
                femaleTeacher += 1
            if i == 0:
                self.addListItemStudentAttendance(f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n", file)

            else:
                self.addListItemStudentAttendance(
                    f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
        self.totalstudents.setText(f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')

    def addListItemStudentAttendance(self, text, link):
        print("correctly added")
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)

        button = QToolButton(widget)
        button.setObjectName(f'button-{link}')
        button.setFont(QFont('times new roman', 12))
        button.setText('PRESENT')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button2 = QToolButton(widget)
        button2.setObjectName(f'button2-{link}')
        button2.setFont(QFont('times new roman', 12))
        button2.setText('ABSENT')
        button2.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button3 = QToolButton(widget)
        button3.setObjectName(f'button3-{link}')
        button3.setFont(QFont('times new roman', 12))
        button3.setText('VIEW')
        button3.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button4 = QToolButton(widget)
        button4.setObjectName(f'button4-{link}')
        button4.setFont(QFont('times new roman', 12))
        button4.setText('LATE')
        button4.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        # here it is
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button3)
        layout.addWidget(button)
        layout.addWidget(button4)
        layout.addWidget(button2)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.presentStudent)

        button2.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button2.clicked.connect(self.absentStudent)

        button3.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button3.clicked.connect(self.new3)

        button4.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button4.clicked.connect(self.lateStudent)

    def new3(self):
        sender = self.sender()
        print(sender.objectName())
        print('one')
        for btn in self.settings_dialog.findChildren(QToolButton):
            print('two')
            # print(btn.text(), len(btn.objectName()))
            if btn.objectName() == sender.objectName():
                print('three')

                button = btn
                link = btn.objectName().split('button3-')[1].strip()
                file = pd.read_csv(link)
                file.to_html("StudentTable.html")
                os.system('StudentTable.html')
                os.system('del StudentTable.html')

    def presentStudent(self):
        try:
            sender = self.sender().objectName().split('button-')[1].strip()
            print(sender, 'present')

            now = datetime.datetime.now()
            date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
            data = pd.read_csv(sender, header=None)
            myclass = data.iloc[3][1].strip()
            print(myclass)
            data = data.to_dict()
            print(data)

            title = date
            data[0][title] = title
            data[1][title] = 'PRESENT'

            df = pd.DataFrame(data)
            # df = df.transpose()

            csv_data = df.to_csv(sender, index=False, header=False)

            date = date.split(":")
            date = '-'.join(date)
            id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

            title2 = date + ' - ' + myclass
            name = sender.split('\\')[1].strip().split('-')[0].strip()

            fhand = open(f'Students Attendance/daily/{title2}.csv', 'a')
            fhand.write(f'{name}, {id}, PRESENT\n')
            fhand.close()
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def lateStudent(self):
        sender = self.sender().objectName().split('button4-')[1].strip()
        print(sender, 'late')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        myclass = data.iloc[3][1]
        print(myclass)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'LATE'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date + ' - ' + myclass
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Students Attendance/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, LATE\n')
        fhand.close()

    def absentStudent(self):
        sender = self.sender().objectName().split('button2-')[1].strip()
        print(sender, 'absent')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        myclass = data.iloc[3][1]
        print(myclass)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'ABSENT'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date + ' - ' + myclass
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Students Attendance/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, ABSENT\n')
        fhand.close()

    def presentStaff(self):
        sender = self.sender().objectName().split('button-')[1].strip()
        print(sender, 'present')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'PRESENT'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Non-Teaching/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, PRESENT\n')
        fhand.close()

    def lateStaff(self):
        sender = self.sender().objectName().split('button4-')[1].strip()
        print(sender, 'late')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'LATE'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Non-Teaching/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, LATE\n')
        fhand.close()

    def absentStaff(self):
        sender = self.sender().objectName().split('button2-')[1].strip()
        print(sender, 'absent')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'ABSENT'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Non-Teaching/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, ABSENT\n')
        fhand.close()

    def presentTeacher(self):
        sender = self.sender().objectName().split('button-')[1].strip()
        print(sender, 'present')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'PRESENT'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Teachers/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, PRESENT\n')
        fhand.close()

    def lateTeacher(self):
        sender = self.sender().objectName().split('button4-')[1].strip()
        print(sender, 'late')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'LATE'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Teachers/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, LATE\n')
        fhand.close()

    def absentTeacher(self):
        sender = self.sender().objectName().split('button2-')[1].strip()
        print(sender, 'absent')

        now = datetime.datetime.now()
        date = str(now.day) + " : " + str(now.month) + " : " + str(now.year)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = date
        data[0][title] = title
        data[1][title] = 'ABSENT'

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)

        date = date.split(":")
        date = '-'.join(date)
        id = sender.split('\\')[1].strip().split('-')[1].strip().split('.')[0].strip()

        title2 = date
        name = sender.split('\\')[1].strip().split('-')[0].strip()


        fhand = open(f'Staff Attendance/Teachers/daily/{title2}.csv', 'a')
        fhand.write(f'{name}, {id}, ABSENT\n')
        fhand.close()

    def addListItem(self, text):
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)
        button = QToolButton(widget)
        button.setObjectName(f'button-{text}')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.new)

    def new(self):
        sender = self.sender()
        print(sender.objectName())
        for btn in self.settings_dialog.findChildren(QToolButton):
            print(btn.text(), len(btn.objectName()))
            if btn.objectName() == sender.objectName():
                btn.objectName()
                button = btn
                button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

    def addToDoListItem(self, text):
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)
        button = QToolButton(widget)
        button.setObjectName(f'button-{text}')
        button.setText("Remove")
        button.setFont(QFont('times new roman', 12))
        button.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.newToDo)

    def newToDo(self):
        try:
            sender = self.sender()
            print(sender.objectName())
            for i, btn in enumerate(self.settings_dialog.findChildren(QToolButton)):
                print(btn.text(), len(btn.objectName()))
                if btn.objectName() == sender.objectName():
                    btn.objectName()
                    button = btn
                    self.students_list.clear()

                    mytext = btn.objectName().split('button-')[1].split('>')[1].lstrip().rstrip()
                    try:
                        mytext = mytext.split('\n')
                        mytext = [item.lstrip().rstrip() for item in mytext]
                        mytext = '\n'.join(mytext)
                    except:
                        print()

                    fhand = open('To Do List.txt', 'r')
                    text = ''
                    for line in fhand:
                        text += line
                    items = text.split('$#&@')
                    fhand.close()

                    for i, item in enumerate(items):
                        print(i, item, mytext)
                        if item.lstrip().rstrip() == mytext:
                            a = items.pop(i)

                    items = '$#&@'.join(items)
                    fhand = open('To Do List.txt', 'w')
                    fhand.write(items)
                    fhand.close()

                    self.listtodos()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def showStaffAttendance(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Staff Daily Attendance")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Staff Daily Attendance")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:khaki; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.hboxRow14 = QHBoxLayout()

            totalTeachers = QPushButton('Teaching Staff')
            totalTeachers.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset yellow; background-color:yellow; text-align:center;")
            totalTeachers.clicked.connect(lambda: self.getStaffAttendance('Staff Attendance/Teachers'))
            self.hboxRow14.addWidget(totalTeachers)

            self.addTeacher = QPushButton('Non-Teaching Staff')
            self.addTeacher.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset skyblue; background-color:skyblue; text-align:center;")
            self.addTeacher.clicked.connect(lambda: self.getStaffAttendance('Staff Attendance/Non-Teaching'))
            self.hboxRow14.addWidget(self.addTeacher)

            self.vbox2.addLayout(self.hboxRow14)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()
            self.getStaffAttendance('Staff Attendance/Non-Teaching')


            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def getStaffAttendance(self, link):
        global maleTeacher
        global femaleTeacher
        self.students_list.clear()
        try:
            maleTeacher = 0
            femaleTeacher = 0
            path = link + '/*.csv'
            files = glob.glob(path)
            for i, file in enumerate(files):
                mydata = pd.read_csv(file, header=None)
                print(mydata)
                if mydata.iloc[11][1] == 'Male':
                    maleTeacher += 1
                elif mydata.iloc[11][1] == 'Female':
                    femaleTeacher += 1
                if i == 0:
                    self.addListItemStaffAttendance(
                        f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)

                else:
                    self.addListItemStaffAttendance(
                        f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)
            self.totalstudents.setText(
                f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def getTeachersAttendance(self):
        global maleTeacher
        global femaleTeacher
        try:
            maleTeacher = 0
            femaleTeacher = 0
            path = 'Staff Attendance/Teachers' + '/*.csv'
            files = glob.glob(path)
            for i, file in enumerate(files):
                mydata = pd.read_csv(file, header=None)
                print(mydata)
                if mydata.iloc[11][1] == 'Male':
                    maleTeacher += 1
                elif mydata.iloc[11][1] == 'Female':
                    femaleTeacher += 1
                if i == 0:
                    self.addListItemTeachersAttendance(
                        f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)

                else:
                    self.addListItemTeachersAttendance(
                        f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)
            self.totalstudents.setText(
                f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def addListItemStaffAttendance(self, text, link):
        print("correctly added")
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)

        button = QToolButton(widget)
        button.setObjectName(f'button-{link}')
        button.setFont(QFont('times new roman', 12))
        button.setText('PRESENT')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button2 = QToolButton(widget)
        button2.setObjectName(f'button2-{link}')
        button2.setFont(QFont('times new roman', 12))
        button2.setText('ABSENT')
        button2.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button3 = QToolButton(widget)
        button3.setObjectName(f'button3-{link}')
        button3.setFont(QFont('times new roman', 12))
        button3.setText('VIEW')
        button3.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button4 = QToolButton(widget)
        button4.setObjectName(f'button4-{link}')
        button4.setFont(QFont('times new roman', 12))
        button4.setText('LATE')
        button4.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button3)
        layout.addWidget(button)
        layout.addWidget(button4)
        layout.addWidget(button2)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.presentStaff)

        button2.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button2.clicked.connect(self.absentStaff)

        button3.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button3.clicked.connect(self.new3)

        button4.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button4.clicked.connect(self.lateStaff)

    def addListItemTeachersAttendance(self, text, link):
        print("correctly added")
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)

        button = QToolButton(widget)
        button.setObjectName(f'button-{link}')
        button.setFont(QFont('times new roman', 12))
        button.setText('PRESENT')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button2 = QToolButton(widget)
        button2.setObjectName(f'button2-{link}')
        button2.setFont(QFont('times new roman', 12))
        button2.setText('ABSENT')
        button2.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button3 = QToolButton(widget)
        button3.setObjectName(f'button3-{link}')
        button3.setFont(QFont('times new roman', 12))
        button3.setText('VIEW')
        button3.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button4 = QToolButton(widget)
        button4.setObjectName(f'button4-{link}')
        button4.setFont(QFont('times new roman', 12))
        button4.setText('LATE')
        button4.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightgray; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")


        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button3)
        layout.addWidget(button)
        layout.addWidget(button4)
        layout.addWidget(button2)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.presentTeacher)

        button2.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button2.clicked.connect(self.absentTeacher)

        button3.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button3.clicked.connect(self.new3)

        button4.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button4.clicked.connect(self.lateTeacher)

    def showTeachingStaff(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Teaching Staff")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Teaching Staff")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            #here

            self.hboxRow14 = QHBoxLayout()

            self.totalTeachers = QLabel(f'\t\tTotal Teaching Staff : {12}\t\tMale : {7}\t\tFemale : {5}\t\t')
            self.totalTeachers.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset aqua; background-color:cyan; text-align:center;")
            self.hboxRow14.addWidget(self.totalTeachers)

            self.addTeacher = QPushButton('ADD TEACHER')
            self.addTeacher.setStyleSheet("font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.addTeacher.clicked.connect(self.addNewTeacher)
            self.hboxRow14.addWidget(self.addTeacher)

            self.vbox2.addLayout(self.hboxRow14)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()

            self.getTeachersData()

            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def getTeachersData(self):
        global maleTeacher
        global femaleTeacher
        maleTeacher = 0
        femaleTeacher = 0
        path = 'Teaching Staff' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print()
            if mydata.iloc[11][1] == 'Male':
                maleTeacher += 1
            elif mydata.iloc[11][1] == 'Female':
                femaleTeacher += 1
            if i == 0:
                self.addListItemTeacher(f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n", file)
            else:
                self.addListItemTeacher(
                    f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
        self.totalTeachers.setText(f'\t\tTotal Teaching Staff : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')

    def addListItemTeacher(self, text, link):
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)
        button = QToolButton(widget)
        button.setObjectName(f'button-{link}')
        button.setFont(QFont('times new roman', 12))
        button.setText('VIEW')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.new1)

    def new1(self):
        sender = self.sender()
        print(sender.objectName())
        for btn in self.settings_dialog.findChildren(QToolButton):
            print(btn.text(), len(btn.objectName()))
            if btn.objectName() == sender.objectName():

                button = btn
                link = btn.objectName().split('button-')[1].strip()
                file = pd.read_csv(link)
                file.to_html("StudentTable.html")
                os.system('StudentTable.html')
                os.system('del StudentTable.html')




    def showMarks(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Marks")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Marks")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orange; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.hboxRow14 = QHBoxLayout()

            self.totalstudents = QLabel(f'\t\tTotal Students : {12}\t\tMale : {7}\t\tFemale : {5}\t\t')
            self.totalstudents.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
            self.hboxRow14.addWidget(self.totalstudents)

            self.addTeacher = QPushButton('ADD Marks By CLASS')
            self.addTeacher.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.addTeacher.clicked.connect(self.addMarks)
            self.hboxRow14.addWidget(self.addTeacher)

            self.vbox2.addLayout(self.hboxRow14)



            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()
            self.getStudentsData()

            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def addAttendance(self):
        print('attendance added')
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        # settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Add New To Do Item")
        settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        settings_dialog.setGeometry(427, 156, 500, 200)

        vbox_master = QVBoxLayout()

        self.textedit = QComboBox()
        self.textedit.setFont(QFont('times new roman', 16))
        fhand = open('Classes.txt', 'r')
        for line in fhand:
            if len(line.strip()) > 0:
                self.textedit.addItem(line.strip())

        vbox_master.addWidget(self.textedit)
        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)
        btn_addNew.clicked.connect(self.hovered1)
        btn_addNew.clicked.connect(lambda: settings_dialog.close())

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

        self.students_list.clear()
        global maleTeacher
        global femaleTeacher
        global Class
        maleTeacher = 0
        femaleTeacher = 0

        path = 'Students Attendance' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print(mydata)
            if mydata.iloc[3][1] == Class:
                if mydata.iloc[11][1] == 'Male':
                    maleTeacher += 1
                elif mydata.iloc[11][1] == 'Female':
                    femaleTeacher += 1
                if i == 0:
                    self.addListItemStudentAttendance(
                    f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
                else:
                    self.addListItemStudentAttendance(
                        f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)

        self.totalstudents.setText(
            f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')


    def addMarks(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        # settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Add New To Do Item")
        settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        settings_dialog.setGeometry(427, 156, 500, 200)

        vbox_master = QVBoxLayout()

        self.textedit = QComboBox()
        self.textedit.setFont(QFont('times new roman', 16))
        fhand = open('Classes.txt', 'r')
        for line in fhand:
            if len(line.strip()) > 0:
                self.textedit.addItem(line.strip())

        vbox_master.addWidget(self.textedit)
        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)
        btn_addNew.clicked.connect(self.hovered1)
        btn_addNew.clicked.connect(lambda: settings_dialog.close())

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

        self.students_list.clear()
        global maleTeacher
        global femaleTeacher
        global Class
        maleTeacher = 0
        femaleTeacher = 0

        path = 'Marks Students' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print(mydata)
            if mydata.iloc[3][1] == Class:
                if mydata.iloc[11][1] == 'Male':
                    maleTeacher += 1
                elif mydata.iloc[11][1] == 'Female':
                    femaleTeacher += 1
                if i == 0:
                    self.addListItemStudent(
                    f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
                else:
                    self.addListItemStudent(
                        f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                        file)

        self.totalstudents.setText(
            f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')

    def hovered1(self):
        global Class
        text = self.textedit.currentText().strip()
        Class = text

    def hovered2(self):
        name = self.line_name.text().strip()
        marks = self.line_name2.text().strip()
        date = self.line_name3.date()
        date = str(date.toPyDate())
        sender = 'Marks Students/' + self.sender().objectName().split('button2-')[1].split('\\')[1]
        print(sender)
        data = pd.read_csv(sender, header=None)
        data = data.to_dict()
        print(data)

        title = name + "   (" + date + ")"
        data[0][title] = title
        data[1][title] = marks

        df = pd.DataFrame(data)
        # df = df.transpose()

        csv_data = df.to_csv(sender, index=False, header=False)


    def addtestMarks(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        # settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Add New To Do Item")
        settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        settings_dialog.setGeometry(427, 156, 500, 200)

        vbox_master = QVBoxLayout()

        vbox1 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)
        vbox_master.addLayout(vbox1)

        self.label_titl = QLabel('Name of Test')
        self.label_titl.setAlignment(Qt.AlignCenter)
        self.label_titl.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
        hbox2.addWidget(self.label_titl)

        self.label_titl2 = QLabel("Marks Scored")
        self.label_titl2.setAlignment(Qt.AlignCenter)
        self.label_titl2.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
        hbox3.addWidget(self.label_titl2)

        self.label_titl3 = QLabel("Test Date")
        self.label_titl3.setAlignment(Qt.AlignCenter)
        self.label_titl3.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
        hbox4.addWidget(self.label_titl3)

        self.line_name = QLineEdit()
        self.line_name.setStyleSheet('background-color:white')
        self.line_name.setFont(QFont('times new roman', 22))
        self.line_name.setAlignment(Qt.AlignCenter)
        hbox2.addWidget(self.line_name)

        self.line_name2 = QLineEdit()
        self.line_name2.setStyleSheet('background-color:white')
        self.line_name2.setFont(QFont('times new roman', 22))
        self.line_name2.setAlignment(Qt.AlignCenter)
        hbox3.addWidget(self.line_name2)

        self.line_name3 = QDateEdit(calendarPopup=True)
        self.line_name3.setDateTime(QDateTime.currentDateTime())
        self.line_name3.setFont(QFont('times new roman', 22))
        self.line_name3.setAlignment(Qt.AlignCenter)
        hbox4.addWidget(self.line_name3)

        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)
        sender = self.sender().objectName()
        btn_addNew.setObjectName(sender)
        btn_addNew.clicked.connect(self.hovered2)
        btn_addNew.clicked.connect(lambda: settings_dialog.close())

        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def getStudentsData(self):
        global maleTeacher
        global femaleTeacher
        maleTeacher = 0
        femaleTeacher = 0
        path = 'Marks Students' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print(mydata)
            if mydata.iloc[11][1] == 'Male':
                maleTeacher += 1
            elif mydata.iloc[11][1] == 'Female':
                femaleTeacher += 1
            if i == 0:
                self.addListItemStudent(f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n", file)
            else:
                self.addListItemStudent(
                    f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
        self.totalstudents.setText(f'\t\tTotal Students : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')

    def addListItemStudent(self, text, link):
        item = QListWidgetItem(text)
        item.setFont(QFont("times new roman", 16))
        self.students_list.addItem(item)
        widget = QWidget(self.students_list)

        button = QToolButton(widget)
        button.setObjectName(f'button-{link}')
        button.setFont(QFont('times new roman', 12))
        button.setText('VIEW')
        button.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

        button2 = QToolButton(widget)
        button2.setObjectName(f'button2-{link}')
        button2.setFont(QFont('times new roman', 12))
        button2.setText('ADD MARKS')
        button2.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:cyan; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")



        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        layout.addWidget(button2)
        self.students_list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button.clicked.connect(self.new2)

        button2.clicked.connect(
            lambda: self.handleButtonClicked(item))
        button2.clicked.connect(self.addtestMarks)



    def new2(self):
        sender = self.sender()
        print(sender.objectName())
        for btn in self.settings_dialog.findChildren(QToolButton):
            # print(btn.text(), len(btn.objectName()))
            if btn.objectName() == sender.objectName():

                button = btn
                link = btn.objectName().split('button-')[1].strip()
                file = pd.read_csv(link)
                file.to_html("StudentTable.html")
                os.system('StudentTable.html')
                os.system('del StudentTable.html')

    def showFinances(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Payment and Finances")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setStyleSheet('background-color: white')
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Payment and Finances")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:orangered; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.hboxRow14 = QHBoxLayout()

            self.btn1 = QPushButton('\nSTUDENTS FEES\n')
            self.btn1.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:orange; text-align:center;")
            self.btn1.clicked.connect(self.fees)
            self.hboxRow14.addWidget(self.btn1)

            self.btn2 = QPushButton('\nDONATIONS\n')
            self.btn2.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:springgreen; text-align:center;")
            self.btn2.clicked.connect(self.donations)
            self.hboxRow14.addWidget(self.btn2)


            self.vbox2.addLayout(self.hboxRow14)

            self.hboxRow15 = QHBoxLayout()

            self.btn3 = QPushButton("\nTEACHERS SALARY\n")
            self.btn3.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:khaki; text-align:center;")
            self.btn3.clicked.connect(self.TeacherSalary)
            self.hboxRow15.addWidget(self.btn3)

            self.btn4 = QPushButton('\nSTAFF SALARY\n')
            self.btn4.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:magenta; text-align:center;")
            self.btn4.clicked.connect(self.StaffSalary)
            self.hboxRow15.addWidget(self.btn4)

            self.vbox2.addLayout(self.hboxRow15)

            self.hboxRow16 = QHBoxLayout()

            self.btn5 = QPushButton('\nBILLS\n')
            self.btn5.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:mediumpurple; text-align:center;")
            self.btn5.clicked.connect(self.bills)
            self.hboxRow16.addWidget(self.btn5)

            self.btn6 = QPushButton('\nEXPENDITURES\n')
            self.btn6.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:skyblue; text-align:center;")
            self.btn6.clicked.connect(self.expenditure)
            self.hboxRow16.addWidget(self.btn6)

            self.vbox2.addLayout(self.hboxRow16)

            self.hboxRow17 = QHBoxLayout()

            self.btn7 = QPushButton('\nBALANCE\n')
            self.btn7.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:pink; text-align:center;")
            self.btn7.clicked.connect(self.balance)
            self.hboxRow17.addWidget(self.btn7)

            self.btn8 = QPushButton('\nFINANCIAL REPORT\n')
            self.btn8.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:yellow; text-align:center;")
            self.btn8.clicked.connect(self.financialReport)
            self.hboxRow17.addWidget(self.btn8)

            self.vbox2.addLayout(self.hboxRow17)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def fees(self):
        try:
            self.settings_dialog2 = QDialog()
            self.settings_dialog2.setModal(True)
            # self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
            self.settings_dialog2.setWindowTitle("        Student Fee")
            self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            self.settings_dialog2.setGeometry(327, 156, 700, 200)

            vbox_master = QVBoxLayout()

            self.lb1 = QLabel("STUDENT FEE")
            self.lb1.setAlignment(Qt.AlignCenter)
            self.lb1.setStyleSheet(
                "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset orange; background-color:orange; text-align:center;")
            vbox_master.addWidget(self.lb1)

            self.lb2 = QLabel("Select Class")
            # self.lb2.setAlignment(Qt.AlignCenter)
            self.lb2.setFont(QFont("times new roman", 22))
            self.lb2.setFixedHeight(48)
            vbox_master.addWidget(self.lb2)

            self.cbox = QComboBox()
            self.cbox.setFont(QFont("times new roman", 16))
            vbox_master.addWidget(self.cbox)

            self.cbox.addItem("ALL")
            fhand = open('Classes.txt', 'r')
            for line in fhand:
                if len(line.strip()) > 0:
                    self.cbox.addItem(line.strip())
            self.cbox.currentIndexChanged.connect(self.classHovered)

            self.lb3 = QLabel("Select Student")
            # self.lb3.setAlignment(Qt.AlignCenter)
            self.lb3.setFont(QFont("times new roman", 22))
            self.lb3.setFixedHeight(48)
            vbox_master.addWidget(self.lb3)

            self.cbox2 = QComboBox()
            self.cbox2.setFont(QFont("times new roman", 16))
            vbox_master.addWidget(self.cbox2)

            files = glob.glob('Payment and Finances/Students/*.csv')

            for line in files:
                item = line.split('/')[-1].strip().split('.')[0].split('-')
                name = item.pop(0).split('\\')[1]

                self.cbox2.addItem(f"{name}    ({''.join(item)})")

            self.lb3 = QLabel("Fee Amount")
            self.lb3.setFont(QFont("times new roman", 22))
            self.lb3.setFixedHeight(48)
            vbox_master.addWidget(self.lb3)

            self.lne2 = QLineEdit()
            self.lne2.setStyleSheet("background-color:white")
            self.lne2.setFont(QFont("times new roman", 22))
            vbox_master.addWidget(self.lne2)

            self.lb3 = QLabel("Fee Payment Date")
            self.lb3.setFont(QFont("times new roman", 22))
            self.lb3.setFixedHeight(48)
            vbox_master.addWidget(self.lb3)

            self.lne3 = QDateEdit(calendarPopup=True)
            self.lne3.setFont(QFont("times new roman", 22))
            self.lne3.setDateTime(QDateTime.currentDateTime())
            self.lne3.setStyleSheet('background-color:white;')
            # self.lne3.setAlignment(Qt.AlignCenter)
            vbox_master.addWidget(self.lne3)

            hbox = QHBoxLayout()

            self.lb4 = QLabel("Method")
            self.lb4.setFont(QFont("times new roman", 22))
            self.lb4.setFixedHeight(63)
            self.lb4.setAlignment(Qt.AlignCenter)
            hbox.addWidget(self.lb4)
            vbox_master.addLayout(hbox)

            self.lne4 = QComboBox()
            self.lne4.setStyleSheet("background-color:skyblue")
            self.lne4.setFont(QFont("times new roman", 22))
            hbox.addWidget(self.lne4)
            self.lne4.addItem("CASH")
            self.lne4.addItem("CARD")
            self.lne4.addItem("ONLINE")
            self.lne4.addItem("OTHER")

            btn_addNew = QPushButton("Submit")
            btn_addNew.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
            btn_addNew.setFixedWidth(372)
            btn_addNew.pressed.connect(self.submitStudentFee)
            btn_addNew.released.connect(lambda: self.settings_dialog2.close())
            hbox = QHBoxLayout()
            hbox.addWidget(btn_addNew)
            vbox_master.addLayout(hbox)

            self.settings_dialog2.setLayout(vbox_master)
            self.settings_dialog2.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")
            print(sys.exc_info()[2], "occurred.")

    def submitStudentFee(self):
        now = datetime.datetime.now()
        rdate = f"  {now.day} / {now.month} / {now.year}  -  {now.hour} : {now.minute} : {now.second}"
        tdate = self.lne3.date()
        tdate = str(tdate.toPyDate())
        myclass = self.cbox.currentText().strip()
        details = "Fee    " + self.cbox2.currentText().strip() + f"    Student ({myclass})"
        method = self.lne4.currentText().strip()
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        amount = self.lne2.text().strip()
        newAmount = ''
        if len(amount.strip()) > 0:
            for i in amount:
                if i in a:
                    newAmount += i

        amount = float(newAmount)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = float(balance)
        balance = balance + amount

        fhand2 = open(link, 'a')
        fhand2.write(f"\n{rdate}, {tdate}, {details}, {method}, {amount}, {balance}")
        fhand2.close()

    def classHovered(self):
        if self.cbox.itemText(0).strip() == 'ALL':
            self.cbox.removeItem(0)
        self.cbox2.clear()

        text = self.cbox.currentText().strip()
        files = glob.glob('Payment and Finances/Students/*.csv')
        for file in files:
            fhand = open(file, 'r')
            fhand = fhand.readlines()
            if fhand[3].split(',')[1].strip() == text:
                self.cbox2.addItem(f"{fhand[0].split(',')[1].strip()}    ({fhand[1].split(',')[1].strip()})")





    def donations(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("       Donations")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("DONATIONS")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setFont(QFont("times new roman", 36))
        self.lb1.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:greenyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        vbox_master.addWidget(self.lb1)

        self.lb2 = QLabel("Donation Details")
        self.lb2.setFont(QFont("times new roman", 22))
        self.lb2.setFixedHeight(48)
        vbox_master.addWidget(self.lb2)

        self.lne = QLineEdit()
        self.lne.setStyleSheet("background-color:white")
        self.lne.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne)

        self.lb3 = QLabel("Donation Amount")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne2 = QLineEdit()
        self.lne2.setStyleSheet("background-color:white")
        self.lne2.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne2)

        self.lb3 = QLabel("Date Donation Received")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne3 = QDateEdit(calendarPopup=True)
        self.lne3.setFont(QFont("times new roman", 22))
        self.lne3.setDateTime(QDateTime.currentDateTime())
        self.lne3.setStyleSheet("Background-color:lightgray")
        # self.lne3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.lne3)

        hbox = QHBoxLayout()

        self.lb4 = QLabel("Method")
        self.lb4.setFont(QFont("times new roman", 22))
        self.lb4.setStyleSheet("background-color:white")
        self.lb4.setFixedHeight(63)
        self.lb4.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.lb4)
        vbox_master.addLayout(hbox)

        self.lne4 = QComboBox()
        self.lne4.setStyleSheet("background-color:yellow")
        self.lne4.setFont(QFont("times new roman", 22))
        hbox.addWidget(self.lne4)
        self.lne4.addItem("CASH")
        self.lne4.addItem("CARD")
        self.lne4.addItem("ONLINE")
        self.lne4.addItem("OTHER")

        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        btn_addNew.pressed.connect(self.submitDonation)
        btn_addNew.released.connect(lambda: self.settings_dialog2.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)

        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()

    def submitDonation(self):
        now = datetime.datetime.now()
        rdate = f"  {now.day} / {now.month} / {now.year}  -  {now.hour} : {now.minute} : {now.second}"
        tdate = self.lne3.date()
        tdate = str(tdate.toPyDate())
        details = self.lne.text().strip()
        method = self.lne4.currentText().strip()
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        amount = self.lne2.text().strip()
        newAmount = ''
        if len(amount.strip()) > 0:
            for i in amount:
                if i in a:
                    newAmount += i

        amount = float(newAmount)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = float(balance)
        balance = balance + amount

        fhand2 = open(link, 'a')
        fhand2.write(f"\n{rdate}, {tdate}, {details}, {method}, {amount}, {balance}")
        fhand2.close()

    def StaffSalary(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("        Staff Salary")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("STAFF SALARY")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset magenta; background-color:magenta; text-align:center;")
        vbox_master.addWidget(self.lb1)


        self.lb3 = QLabel("Select Person")
        # self.lb3.setAlignment(Qt.AlignCenter)
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.cbox2 = QComboBox()
        self.cbox2.setFont(QFont("times new roman", 16))
        self.cbox2.setStyleSheet("background-color:white")
        vbox_master.addWidget(self.cbox2)

        files = glob.glob('Payment and Finances/Staff/*.csv')

        for line in files:
            item = line.split('/')[-1].strip().split('.')[0].split('-')
            name = item.pop(0).split('\\')[1]

            self.cbox2.addItem(f"{name}    ({''.join(item)})")


        self.lb3 = QLabel("Salary Amount")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne2 = QLineEdit()
        self.lne2.setStyleSheet("background-color:white")
        self.lne2.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne2)

        self.lb3 = QLabel("Salary Payment Date")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne3 = QDateEdit(calendarPopup=True)
        self.lne3.setFont(QFont("times new roman", 22))
        self.lne3.setDateTime(QDateTime.currentDateTime())
        self.lne3.setStyleSheet('background-color:white;')
        # self.lne3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.lne3)

        hbox = QHBoxLayout()

        self.lb4 = QLabel("Method")
        self.lb4.setFont(QFont("times new roman", 22))
        self.lb4.setFixedHeight(63)
        self.lb4.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.lb4)
        vbox_master.addLayout(hbox)

        self.lne4 = QComboBox()
        self.lne4.setStyleSheet("background-color:skyblue")
        self.lne4.setFont(QFont("times new roman", 22))
        hbox.addWidget(self.lne4)
        self.lne4.addItem("CASH")
        self.lne4.addItem("CARD")
        self.lne4.addItem("ONLINE")
        self.lne4.addItem("OTHER")

        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        btn_addNew.pressed.connect(self.submitSalaryStaff)
        btn_addNew.released.connect(lambda: self.settings_dialog2.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)

        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()


    def submitSalaryStaff(self):
        now = datetime.datetime.now()
        rdate = f"  {now.day} / {now.month} / {now.year}  -  {now.hour} : {now.minute} : {now.second}"
        tdate = self.lne3.date()
        tdate = str(tdate.toPyDate())
        details = "Salary    " + self.cbox2.currentText().strip() + "    Staff"
        method = self.lne4.currentText().strip()
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        amount = self.lne2.text().strip()
        newAmount = ''
        if len(amount.strip()) > 0:
            for i in amount:
                if i in a:
                    newAmount += i

        amount = float(newAmount)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = float(balance)
        balance = balance - amount

        fhand2 = open(link, 'a')
        fhand2.write(f"\n{rdate}, {tdate}, {details}, {method}, {amount}, {balance}")
        fhand2.close()

    def submitSalaryTeacher(self):
        now = datetime.datetime.now()
        rdate = f"  {now.day} / {now.month} / {now.year}  -  {now.hour} : {now.minute} : {now.second}"
        tdate = self.lne3.date()
        tdate = str(tdate.toPyDate())
        details = "Salary    " + self.cbox2.currentText().strip() + "    Teacher"
        method = self.lne4.currentText().strip()
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        amount = self.lne2.text().strip()
        newAmount = ''
        if len(amount.strip()) > 0:
            for i in amount:
                if i in a:
                    newAmount += i

        amount = float(newAmount)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = float(balance)
        balance = balance - amount

        fhand2 = open(link, 'a')
        fhand2.write(f"\n{rdate}, {tdate}, {details}, {method}, {amount}, {balance}")
        fhand2.close()

    def TeacherSalary(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("       Teachers' Salary")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("TEACHER SALARY")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset khaki; background-color:khaki; text-align:center;")
        vbox_master.addWidget(self.lb1)

        self.lb3 = QLabel("Select Teacher")
        # self.lb3.setAlignment(Qt.AlignCenter)
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.cbox2 = QComboBox()
        self.cbox2.setFont(QFont("times new roman", 16))
        self.cbox2.setStyleSheet("background-color:white")
        vbox_master.addWidget(self.cbox2)

        files = glob.glob('Payment and Finances/Teachers/*.csv')

        for line in files:
            item = line.split('/')[-1].strip().split('.')[0].split('-')
            name = item.pop(0).split('\\')[1]

            self.cbox2.addItem(f"{name}    ({''.join(item)})")

        self.lb3 = QLabel("Salary Amount")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne2 = QLineEdit()
        self.lne2.setStyleSheet("background-color:white")
        self.lne2.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne2)

        self.lb3 = QLabel("Salary Payment Date")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne3 = QDateEdit(calendarPopup=True)
        self.lne3.setFont(QFont("times new roman", 22))
        self.lne3.setDateTime(QDateTime.currentDateTime())
        self.lne3.setStyleSheet('background-color:white;')
        # self.lne3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.lne3)

        hbox = QHBoxLayout()

        self.lb4 = QLabel("Method")
        self.lb4.setFont(QFont("times new roman", 22))
        self.lb4.setFixedHeight(63)
        self.lb4.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.lb4)
        vbox_master.addLayout(hbox)

        self.lne4 = QComboBox()
        self.lne4.setStyleSheet("background-color:skyblue")
        self.lne4.setFont(QFont("times new roman", 22))
        hbox.addWidget(self.lne4)
        self.lne4.addItem("CASH")
        self.lne4.addItem("CARD")
        self.lne4.addItem("ONLINE")
        self.lne4.addItem("OTHER")

        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        btn_addNew.pressed.connect(self.submitSalaryTeacher)
        btn_addNew.released.connect(lambda: self.settings_dialog2.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)

        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()

    def bills(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("       Bills")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("BILLS")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset mediumpurple; background-color:mediumpurple; text-align:center;")
        vbox_master.addWidget(self.lb1)

        self.lb2 = QLabel("Details Of Bill")
        self.lb2.setFont(QFont("times new roman", 22))
        self.lb2.setFixedHeight(48)
        vbox_master.addWidget(self.lb2)

        self.lne = QLineEdit()
        self.lne.setStyleSheet("background-color:white")
        self.lne.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne)

        self.lb3 = QLabel("Bill Amount")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne2 = QLineEdit()
        self.lne2.setStyleSheet("background-color:white")
        self.lne2.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne2)

        self.lb3 = QLabel("Bill Payment Date")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne3 = QDateEdit(calendarPopup=True)
        self.lne3.setFont(QFont("times new roman", 22))
        self.lne3.setDateTime(QDateTime.currentDateTime())
        self.lne3.setStyleSheet('background-color:khaki;')
        # self.lne3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.lne3)

        hbox = QHBoxLayout()

        self.lb4 = QLabel("Method")
        self.lb4.setFont(QFont("times new roman", 22))
        self.lb4.setFixedHeight(63)
        self.lb4.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.lb4)
        vbox_master.addLayout(hbox)

        self.lne4 = QComboBox()
        # self.lne4.setStyleSheet("background-color:white")
        self.lne4.setFont(QFont("times new roman", 22))
        hbox.addWidget(self.lne4)
        self.lne4.addItem("CASH")
        self.lne4.addItem("CARD")
        self.lne4.addItem("ONLINE")
        self.lne4.addItem("OTHER")

        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        btn_addNew.pressed.connect(self.submitExpenditure)
        btn_addNew.released.connect(lambda: self.settings_dialog2.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)

        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()



    def expenditure(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        # self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("       Expenditure")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(372, 72, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("EXPENDITURE")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setFont(QFont('times new roman', 36))
        self.lb1.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:skyblue; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        vbox_master.addWidget(self.lb1)

        self.lb2 = QLabel("Expenditure Details")
        self.lb2.setFont(QFont("times new roman", 22))
        self.lb2.setFixedHeight(48)
        vbox_master.addWidget(self.lb2)

        self.lne = QLineEdit()
        self.lne.setStyleSheet("background-color:white")
        self.lne.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne)

        self.lb3 = QLabel("Expenditure Amount")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne2 = QLineEdit()
        self.lne2.setStyleSheet("background-color:white")
        self.lne2.setFont(QFont("times new roman", 22))
        vbox_master.addWidget(self.lne2)

        self.lb3 = QLabel("Date of Expenditure")
        self.lb3.setFont(QFont("times new roman", 22))
        self.lb3.setFixedHeight(48)
        vbox_master.addWidget(self.lb3)

        self.lne3 = QDateEdit(calendarPopup=True)
        self.lne3.setFont(QFont("times new roman", 22))
        self.lne3.setDateTime(QDateTime.currentDateTime())
        self.lne3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.lne3)

        hbox = QHBoxLayout()

        self.lb4 = QLabel("Method")
        self.lb4.setFont(QFont("times new roman", 22))
        self.lb4.setFixedHeight(63)
        self.lb4.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.lb4)
        vbox_master.addLayout(hbox)

        self.lne4 = QComboBox()
        # self.lne4.setStyleSheet("background-color:white")
        self.lne4.setFont(QFont("times new roman", 22))
        hbox.addWidget(self.lne4)
        self.lne4.addItem("CASH")
        self.lne4.addItem("CARD")
        self.lne4.addItem("ONLINE")
        self.lne4.addItem("OTHER")


        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet(
            "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        btn_addNew.pressed.connect(self.submitExpenditure)
        btn_addNew.released.connect(lambda: self.settings_dialog2.close())
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)

        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()

    def submitExpenditure(self):
        now = datetime.datetime.now()
        rdate = f"  {now.day} / {now.month} / {now.year}  -  {now.hour} : {now.minute} : {now.second}"
        tdate = self.lne3.date()
        tdate = str(tdate.toPyDate())
        details = self.lne.text().strip()
        method = self.lne4.currentText().strip()
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        amount = self.lne2.text().strip()
        newAmount = ''
        if len(amount.strip()) > 0:
            for i in amount:
                if i in a:
                    newAmount += i

        amount = float(newAmount)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = float(balance)
        balance = balance - amount

        fhand2 = open(link, 'a')
        fhand2.write(f"\n{rdate}, {tdate}, {details}, {method}, {amount}, {balance}")
        fhand2.close()



    def balance(self):
        self.settings_dialog2 = QDialog()
        self.settings_dialog2.setModal(True)
        self.settings_dialog2.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog2.setWindowTitle("       Balance")
        self.settings_dialog2.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog2.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.lb1 = QLabel("BALANCE")
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setStyleSheet(
            "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset pink; background-color:pink; text-align:center;")
        vbox_master.addWidget(self.lb1)

        link = "Payment and Finances/financialReport.csv"
        fhand = open(link, 'r')
        fhand = fhand.readlines()
        balance = fhand[-1].split(',')[-1]
        balance = '£' + str(balance)

        self.lb1 = QLabel(balance)
        self.lb1.setAlignment(Qt.AlignCenter)
        self.lb1.setStyleSheet(
            "font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset magenta; background-color:violet; text-align:center;")
        vbox_master.addWidget(self.lb1)


        self.settings_dialog2.setLayout(vbox_master)
        self.settings_dialog2.exec_()

    def financialReport(self):
        link = "Payment and Finances/financialReport.csv"
        file = pd.read_csv(link)
        file.to_html("FinancialReport.html")
        os.system('FinancialReport.html')
        os.system('del FinancialReport.html')

    def showClassTimetable(self):
        return

        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Class Timetable")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Class Timetable")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:yellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()
            for i in range(1212):
                self.addListItem(f"Muhammad Mohib{i+1}")

            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")


    def showThingsToDo(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Things To Do")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Things to do")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:magenta; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()

            self.listtodos()

            self.vbox2.addWidget(self.students_list)

            self.btn_addNew = QPushButton("ADD NEW")
            self.btn_addNew.setStyleSheet("font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.btn_addNew.setFixedWidth(372)
            self.btn_addNew.clicked.connect(self.addNewItem)
            hbox1 = QHBoxLayout()
            hbox1.addWidget(self.btn_addNew)
            hbox1.setAlignment(Qt.AlignRight)
            self.vbox2.addLayout(hbox1)


            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def addNewItem(self):
        settings_dialog = QDialog()
        settings_dialog.setModal(True)
        settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        settings_dialog.setWindowTitle("Add New To Do Item")
        settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        settings_dialog.setGeometry(427, 156, 500, 200)

        vbox_master = QVBoxLayout()

        textedit = QTextEdit()
        textedit.setStyleSheet('background-color:white')
        textedit.setFont(QFont('times new roman', 12))
        vbox_master.addWidget(textedit)
        btn_addNew = QPushButton("Submit")
        btn_addNew.setStyleSheet("font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset springgreen; background-color:#0eeb37; text-align:center;")
        btn_addNew.setFixedWidth(372)
        hbox = QHBoxLayout()
        hbox.addWidget(btn_addNew)
        vbox_master.addLayout(hbox)
        btn_addNew.clicked.connect(lambda: self.registerItem(textedit.toPlainText().strip()))
        btn_addNew.clicked.connect(lambda: settings_dialog.close())


        settings_dialog.setLayout(vbox_master)
        settings_dialog.exec_()

    def registerItem(self, text):
        fhand = open('To Do List.txt', 'a')
        text = text + '$#&@'
        fhand.write(text)
        fhand.close()
        self.students_list.clear()
        self.listtodos()


    def listtodos(self):
        fhand = open('To Do List.txt', 'r')
        text = ''
        for line in fhand:
            text += line
        items = text.split('$#&@')

        for i, item in enumerate(items):
            item = item.lstrip().rstrip()
            item = item.split('\n')
            a = item.pop(0)
            item = '\n      '.join(item)
            item = a + '\n      ' + item
            if len(item.strip()) > 0:
                if i == 0:
                    self.addToDoListItem(f"\n>    {item}")

                else:
                    self.addToDoListItem(f">    {item}")


    def showOthers(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Others")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Others")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:greenyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.mylabel = QLabel()
            self.mylabel.setStyleSheet("font-family:times new roman; font-size: 36px; border-radius: 1cm; border-color:cyan; border: 14px inset cyan; background-color:palegreen; text-align:center;")
            self.mylabel.setText("\tFor More Features, kindly Contact Developers\n\n\t\tQ N SOFTWARE SERVICES\n\n\t\tEmail :\tqnsoftwareservices12272@gmailcom\n\n\t\tWhatsApp : \t+923335212460\n\n\n\t\tYou will always find us at your service\n\n\n\n\tThanks Alot for choosing us")
            self.mylabel.setAlignment(Qt.AlignCenter)
            self.vbox2.addWidget(self.mylabel)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")


    def showNonTeachingStaff(self):
        global panel_status2
        panel_status2 = False
        try:
            self.settings_dialog.close()
        except:
            print()

        try:
            self.settings_dialog = QDialog()
            self.settings_dialog.setModal(True)
            self.settings_dialog.setWindowTitle("    Non-Teaching Staff")
            self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
            # self.settings_dialog.setGeometry(327, 156, 700, 200)
            self.settings_dialog.showFullScreen()
            vbox_master = QVBoxLayout()
            self.vbox2 = QVBoxLayout()

            self.label_title2 = QLabel("Non-Teaching Staff")
            self.label_title2.setAlignment(Qt.AlignCenter)
            self.label_title2.setFont(QFont("times new roman", 22))
            self.label_title2.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:mediumpurple; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.label_title2.setFixedHeight(63)
            self.vbox2.addWidget(self.label_title2)

            self.hboxRow14 = QHBoxLayout()

            self.totalstaff = QLabel(f'\t\tTotal Non-Teaching Staff : {12}\t\tMale : {7}\t\tFemale : {5}\t\t')
            self.totalstaff.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset aqua; background-color:cyan; text-align:center;")
            self.hboxRow14.addWidget(self.totalstaff)

            self.addStaff = QPushButton('ADD STAFF')
            self.addStaff.setStyleSheet(
                "font-family:times new roman; font-size: 22px; border-radius: 1cm; border-color:cyan; border: 14px inset palegreen; background-color:#0eeb37; text-align:center;")
            self.addStaff.clicked.connect(self.addNewStaff)
            self.hboxRow14.addWidget(self.addStaff)

            self.vbox2.addLayout(self.hboxRow14)

            self.label3 = QLabel()
            now = datetime.datetime.now()
            day1 = now.weekday()
            if day1 == 0:
                day1 = 'Monday'
            elif day1 == 1:
                day1 = 'Tuesday'
            elif day1 == 2:
                day1 = 'Wednesday'
            elif day1 == 3:
                day1 = 'Thursday'
            elif day1 == 4:
                day1 = 'Friday'
            elif day1 == 5:
                day1 = 'Saturday'
            elif day1 == 6:
                day1 = 'Sunday'
            self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")
            self.label3.setAlignment(Qt.AlignLeft)
            self.label3.setFont(QFont("times new roman", 22))
            self.label3.setFixedHeight(44)
            self.label3.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:lightyellow; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            vbox_master.addWidget(self.label3)  # lightgray, khaki, lightblue, lightyellow

            self.vbox_side2 = QVBoxLayout()
            self.vbox_side_content2 = QVBoxLayout()

            self.btn1229 = QPushButton()
            self.btn1229.setFixedWidth(63)
            self.btn1229.setIcon(QIcon('School Management Icons/university_library.ico'))
            self.btn1229.setIconSize(QSize(60, 60))
            self.btn1229.clicked.connect(self.panel2)
            self.vbox_side2.addWidget(self.btn1229)

            self.btn1102 = QPushButton(' Dashboard ')
            self.btn1102.setFont(QFont("Sanserif", 16))
            self.btn1102.setFixedWidth(227)
            self.btn1102.clicked.connect(self.showDashboard)
            self.btn1102.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1102)
            self.btn1102.hide()

            self.btn1112 = QPushButton('Student Admission')
            self.btn1112.setFont(QFont("Sanserif", 16))
            self.btn1112.setFixedWidth(227)
            self.btn1112.clicked.connect(self.showStudentAdmission)
            self.btn1112.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1112)
            self.btn1112.hide()

            self.btn1122 = QPushButton('Teaching Staff')
            self.btn1122.setFont(QFont("Sanserif", 16))
            self.btn1122.setFixedWidth(227)
            self.btn1122.clicked.connect(self.showTeachingStaff)
            self.btn1122.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1122)
            self.btn1122.hide()

            self.btn1132 = QPushButton('Non-Teaching Staff ')
            self.btn1132.setFont(QFont("Sanserif", 16))
            self.btn1132.setFixedWidth(227)
            self.btn1132.clicked.connect(self.showNonTeachingStaff)
            self.btn1132.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1132)
            self.btn1132.hide()

            self.btn1142 = QPushButton('Marks')
            self.btn1142.setFont(QFont("Sanserif", 16))
            self.btn1142.setFixedWidth(227)
            self.btn1142.clicked.connect(self.showMarks)
            self.btn1142.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1142)
            self.btn1142.hide()

            self.btn1152 = QPushButton('Students Attendance')
            self.btn1152.setFont(QFont("Sanserif", 16))
            self.btn1152.setFixedWidth(227)
            self.btn1152.clicked.connect(self.showStudentAttendance)
            self.btn1152.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1152)
            self.btn1152.hide()

            self.btn1162 = QPushButton('Staff Attendance')
            self.btn1162.setFont(QFont("Sanserif", 16))
            self.btn1162.setFixedWidth(227)
            self.btn1162.clicked.connect(self.showStaffAttendance)
            self.btn1162.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1162)
            self.btn1162.hide()

            self.btn1172 = QPushButton('Payment / Finances')
            self.btn1172.setFont(QFont("Sanserif", 16))
            self.btn1172.setFixedWidth(227)
            self.btn1172.clicked.connect(self.showFinances)
            self.btn1172.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1172)
            self.btn1172.hide()

            self.btn1182 = QPushButton('Class Timetable')
            self.btn1182.setFont(QFont("Sanserif", 16))
            self.btn1182.setFixedWidth(227)
            self.btn1182.clicked.connect(self.showClassTimetable)
            self.btn1182.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1182)
            self.btn1182.hide()

            self.btn1192 = QPushButton('Things To Do')
            self.btn1192.setFont(QFont("Sanserif", 16))
            self.btn1192.setFixedWidth(227)
            self.btn1192.clicked.connect(self.showThingsToDo)
            self.btn1192.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn1192)
            self.btn1192.hide()

            self.btn11992 = QPushButton('Others')
            self.btn11992.setFont(QFont("Sanserif", 16))
            self.btn11992.setFixedWidth(227)
            self.btn11992.clicked.connect(self.showOthers)
            self.btn11992.setStyleSheet(
                "text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
            self.vbox_side_content2.addWidget(self.btn11992)
            self.btn11992.hide()

            # creating a timer object
            self.timer2 = QTimer()

            # adding action to timer
            self.timer2.timeout.connect(self.changeTime2)

            # update the timer every tenth second
            self.timer2.start(1000)

            self.students_list = QListWidget()
            self.getStaffData()

            self.vbox2.addWidget(self.students_list)

            self.hbox2 = QHBoxLayout()
            self.vbox_side2.addLayout(self.vbox_side_content2)
            self.hbox2.addLayout(self.vbox_side2)
            self.hbox2.addLayout(self.vbox2)
            vbox_master.addLayout(self.hbox2)
            self.settings_dialog.setLayout(vbox_master)
            self.settings_dialog.exec_()

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

    def getStaffData(self):
        global maleTeacher
        global femaleTeacher
        maleTeacher = 0
        femaleTeacher = 0
        path = 'Non-Teaching Staff' + '/*.csv'
        files = glob.glob(path)
        for i, file in enumerate(files):
            mydata = pd.read_csv(file, header=None)
            print()
            if mydata.iloc[11][1] == 'Male':
                maleTeacher += 1
            elif mydata.iloc[11][1] == 'Female':
                femaleTeacher += 1
            if i == 0:
                self.addListItemTeacher(
                    f"\n>\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
            else:
                self.addListItemTeacher(
                    f">\t{mydata.iloc[0][1]} \t ({mydata.iloc[1][1]})\t{mydata.iloc[3][1]} ({mydata.iloc[2][1]}) \t {mydata.iloc[10][0]} {mydata.iloc[10][1]}\n",
                    file)
        self.totalstaff.setText(f'\t\tTotal Non-Teaching Staff : {maleTeacher + femaleTeacher}\t\tMale : {maleTeacher}\t\tFemale : {femaleTeacher}\t\t')

    def handleButtonClicked(self, item):
        print(item.text())

    def changeTime(self):
        now = datetime.datetime.now()
        day1 = now.weekday()
        if day1 == 0:
            day1 = 'Monday'
        elif day1 == 1:
            day1 = 'Tuesday'
        elif day1 == 2:
            day1 = 'Wednesday'
        elif day1 == 3:
            day1 = 'Thursday'
        elif day1 == 4:
            day1 = 'Friday'
        elif day1 == 5:
            day1 = 'Saturday'
        elif day1 == 6:
            day1 = 'Sunday'
        self.label.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")

    def changeTime2(self):
        now = datetime.datetime.now()
        day1 = now.weekday()
        if day1 == 0:
            day1 = 'Monday'
        elif day1 == 1:
            day1 = 'Tuesday'
        elif day1 == 2:
            day1 = 'Wednesday'
        elif day1 == 3:
            day1 = 'Thursday'
        elif day1 == 4:
            day1 = 'Friday'
        elif day1 == 5:
            day1 = 'Saturday'
        elif day1 == 6:
            day1 = 'Sunday'
        self.label3.setText(f"School Management Software\t\t\t                       {now.hour}:{now.minute}:{now.second} \t {now.day} : {now.month} : {now.year}  -  {day1}")

    def newStudent(self):
        try:
            name = self.line_edit_StudentName.text().lstrip().rstrip()
            nr = self.line_edit_StudentNR.text().lstrip().rstrip()
            fathersName = self.line_edit_FathersName.text().lstrip().rstrip()
            fathersNr = self.line_edit_FathersNR.text().lstrip().rstrip()
            mothersName = self.line_edit_MothersName.text().lstrip().rstrip()
            mothersNr = self.line_edit_MothersNR.text().lstrip().rstrip()
            address = self.address_text.toPlainText().lstrip().rstrip()
            postCode = self.line_edit_PostCode.text().lstrip().rstrip()
            email = self.line_edit_Email.text().lstrip().rstrip()
            shift = self.Shift_list.currentText().lstrip().rstrip()
            comments = self.comments_student.toPlainText().lstrip().rstrip()

            category = self.Category_cbox.currentText().lstrip().rstrip()
            gender = self.Gender_cbox.currentText().lstrip().rstrip()
            dob = self.DateOfBirth.date()
            dob = dob.toPyDate()
            telephone = self.line_edit_Telephone.text().lstrip().rstrip()
            fathersEmail = self.line_edit_FathersEmail.text().lstrip().rstrip()
            mothersEmail = self.line_edit_MothersEmail.text().lstrip().rstrip()
            GPname = self.line_edit_GPName.text().lstrip().rstrip()
            GPtelephone = self.line_edit_GPTelephone.text().lstrip().rstrip()
            Class = self.line_edit_Class.currentText().strip()



            mydata = {
                'Name': ['Name', name],
                'Nr': ['Number / ID', nr],
                "Shift": ["Shift", shift],
                "Class": ["Class", Class],
                "Father's Name": ["Father's Name", fathersName],
                "Father's Nr": ["Father's Nr", fathersNr],
                "Father's Email": ["Father's Email", fathersEmail],
                "Mother's Name": ["Mother's Name", mothersName],
                "Mother's Nr": ["Mother's Nr", mothersNr],
                "Mother's Email": ["Mother's Email", mothersEmail],
                "Category": ["Category", category],
                "Gender": ["Gender", gender],
                "Date Of Birth": ["Date Of Birth", dob],
                "Telephone": ["Telephone", telephone],
                "Address": ["Address", address],
                "Postal Code": ["Postal Code", postCode],
                "Email": ["Email", email],
                "G.P's Name": ["G.P's Name", GPname],
                "G.P's Telephone": ["G.P's Telephone", GPtelephone],
                "Comments for Student": ["Comments for Student", comments]
            }

            # my_df = {'Name': name,
            #          'ID': [1, 2],
            #          'Age': [20, 19]}
            df = pd.DataFrame(mydata)
            df = df.transpose()

            # displaying the DataFrame
            print('DataFrame:\n', df)

            title = name + '-' + nr

            # saving the DataFrame as a CSV file
            csv_data = df.to_csv(f'students/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Payment and Finances/Students/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Marks Students/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Students Attendance/{title}.csv', index=False, header=False)

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

        self.showDashboard()

    def newTeacher(self):
        try:
            name = self.line_edit_StudentName.text().lstrip().rstrip()
            nr = self.line_edit_StudentNR.text().lstrip().rstrip()
            fathersName = self.line_edit_FathersName.text().lstrip().rstrip()
            fathersNr = self.line_edit_FathersNR.text().lstrip().rstrip()
            mothersName = self.line_edit_MothersName.text().lstrip().rstrip()
            mothersNr = self.line_edit_MothersNR.text().lstrip().rstrip()
            address = self.address_text.toPlainText().lstrip().rstrip()
            postCode = self.line_edit_PostCode.text().lstrip().rstrip()
            email = self.line_edit_Email.text().lstrip().rstrip()
            shift = self.line_edit_Shift.text().lstrip().rstrip()
            comments = self.comments_student.toPlainText().lstrip().rstrip()

            mobile = self.line_edit_mobile.text().lstrip().rstrip()
            gender = self.Gender_cbox.currentText().lstrip().rstrip()
            dob = self.DateOfBirth.date()
            dob = dob.toPyDate()
            telephone = self.line_edit_Telephone.text().lstrip().rstrip()
            fathersEmail = self.line_edit_FathersEmail.text().lstrip().rstrip()
            mothersEmail = self.line_edit_MothersEmail.text().lstrip().rstrip()
            GPname = self.line_edit_GPName.text().lstrip().rstrip()
            GPtelephone = self.line_edit_GPTelephone.text().lstrip().rstrip()
            designation = self.line_edit_Designation.text().lstrip().rstrip()

            mydata = {
                'Name': ['Name', name],
                'Nr': ['ID', nr],
                "Shift": ["Shift", shift],
                "Designation": ["Designation", designation],
                "Father's Name": ["Father's Name", fathersName],
                "Father's Nr": ["Father's Mobile", fathersNr],
                "Father's Email": ["Father's Email", fathersEmail],
                "Mother's Name": ["Next Of Kin : Name", mothersName],
                "Mother's Nr": ["Next Of Kin : Mobile", mothersNr],
                "Mother's Email": ["Next Of Kin : Email", mothersEmail],
                "Mobile #": ["Mobile #", mobile],
                "Gender": ["Gender", gender],
                "Date Of Birth": ["Date Of Birth", dob],
                "Telephone": ["Telephone", telephone],
                "Address": ["Address", address],
                "Postal Code": ["Postal Code", postCode],
                "Email": ["Email", email],
                "G.P's Name": ["G.P's Name", GPname],
                "G.P's Telephone": ["G.P's Telephone", GPtelephone],
                "Comments for Student": ["Description / Resume / Comments", comments]
            }

            # my_df = {'Name': name,
            #          'ID': [1, 2],
            #          'Age': [20, 19]}
            df = pd.DataFrame(mydata)
            df = df.transpose()

            # displaying the DataFrame
            print('DataFrame:\n', df)

            title = name + '-' + nr

            # saving the DataFrame as a CSV file
            csv_data = df.to_csv(f'Teaching Staff/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Staff Attendance/Teachers/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Payment and Finances/Teachers/{title}.csv', index=False, header=False)

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

        self.showDashboard()

    def newStaff(self):
        try:
            name = self.line_edit_StudentName.text().lstrip().rstrip()
            nr = self.line_edit_StudentNR.text().lstrip().rstrip()
            fathersName = self.line_edit_FathersName.text().lstrip().rstrip()
            fathersNr = self.line_edit_FathersNR.text().lstrip().rstrip()
            mothersName = self.line_edit_MothersName.text().lstrip().rstrip()
            mothersNr = self.line_edit_MothersNR.text().lstrip().rstrip()
            address = self.address_text.toPlainText().lstrip().rstrip()
            postCode = self.line_edit_PostCode.text().lstrip().rstrip()
            email = self.line_edit_Email.text().lstrip().rstrip()
            shift = self.line_edit_Shift.text().lstrip().rstrip()
            comments = self.comments_student.toPlainText().lstrip().rstrip()

            mobile = self.line_edit_mobile.text().lstrip().rstrip()
            gender = self.Gender_cbox.currentText().lstrip().rstrip()
            dob = self.DateOfBirth.date()
            dob = dob.toPyDate()
            telephone = self.line_edit_Telephone.text().lstrip().rstrip()
            fathersEmail = self.line_edit_FathersEmail.text().lstrip().rstrip()
            mothersEmail = self.line_edit_MothersEmail.text().lstrip().rstrip()
            GPname = self.line_edit_GPName.text().lstrip().rstrip()
            GPtelephone = self.line_edit_GPTelephone.text().lstrip().rstrip()
            designation = self.line_edit_Designation.text().lstrip().rstrip()

            mydata = {
                'Name': ['Name', name],
                'Nr': ['ID', nr],
                "Shift": ["Shift", shift],
                "Designation": ["Designation", designation],
                "Father's Name": ["Father's Name", fathersName],
                "Father's Nr": ["Father's Mobile", fathersNr],
                "Father's Email": ["Father's Email", fathersEmail],
                "Mother's Name": ["Next Of Kin : Name", mothersName],
                "Mother's Nr": ["Next Of Kin : Mobile", mothersNr],
                "Mother's Email": ["Next Of Kin : Email", mothersEmail],
                "Mobile #": ["Mobile #", mobile],
                "Gender": ["Gender", gender],
                "Date Of Birth": ["Date Of Birth", dob],
                "Telephone": ["Telephone", telephone],
                "Address": ["Address", address],
                "Postal Code": ["Postal Code", postCode],
                "Email": ["Email", email],
                "G.P's Name": ["G.P's Name", GPname],
                "G.P's Telephone": ["G.P's Telephone", GPtelephone],
                "Comments for Student": ["Description / Resume / Comments", comments]
            }

            # my_df = {'Name': name,
            #          'ID': [1, 2],
            #          'Age': [20, 19]}
            df = pd.DataFrame(mydata)
            df = df.transpose()

            # displaying the DataFrame
            print('DataFrame:\n', df)

            title = name + '-' + nr

            # saving the DataFrame as a CSV file
            csv_data = df.to_csv(f'Non-Teaching Staff/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Staff Attendance/Non-Teaching/{title}.csv', index=False, header=False)
            csv_data = df.to_csv(f'Payment and Finances/Staff/{title}.csv', index=False, header=False)

        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print(sys.exc_info()[1], "occurred.")

        self.showDashboard()

    def btn4(self):
        print('Button 4 clicked')

    def panel(self):
        global panel_status
        if panel_status:
            self.btn110.hide()
            self.btn111.hide()
            self.btn112.hide()
            self.btn113.hide()
            self.btn114.hide()
            self.btn115.hide()
            self.btn116.hide()
            self.btn117.hide()
            self.btn118.hide()
            self.btn119.hide()
            self.btn1199.hide()
            self.btn119922.hide()
            self.btn9212.setFixedWidth(63)

            panel_status = False

        else:
            self.btn110.show()
            self.btn111.show()
            self.btn112.show()
            self.btn113.show()
            self.btn114.show()
            self.btn115.show()
            self.btn116.show()
            self.btn117.show()
            self.btn118.show()
            self.btn119.show()
            self.btn1199.show()
            self.btn119922.show()
            self.btn9212.setFixedWidth(227)
            panel_status = True

    def panel2(self):
        global panel_status2
        if panel_status2:
            self.btn1102.hide()
            self.btn1112.hide()
            self.btn1122.hide()
            self.btn1132.hide()
            self.btn1142.hide()
            self.btn1152.hide()
            self.btn1162.hide()
            self.btn1172.hide()
            self.btn1182.hide()
            self.btn1192.hide()
            self.btn11992.hide()
            self.btn1229.setFixedWidth(63)

            panel_status2 = False

        else:
            self.btn1102.show()
            self.btn1112.show()
            self.btn1122.show()
            self.btn1132.show()
            self.btn1142.show()
            self.btn1152.show()
            self.btn1162.show()
            self.btn1172.show()
            self.btn1182.show()
            self.btn1192.show()
            self.btn11992.show()
            self.btn1229.setFixedWidth(227)
            panel_status2 = True



# fuction called to close the software
    def closew(self):
        self.close()

# fuction called to minimize the software window
    def minimizew(self):
        self.showMinimized()

    def login(self):
        self.settings_dialog3 = QDialog()
        self.settings_dialog3.setModal(True)
        self.settings_dialog3.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog3.setWindowTitle("        LOGIN")
        self.settings_dialog3.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog3.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.labelLogin = QLabel("ENTER PASSWORD")
        self.labelLogin.setFont(QFont("times new roman", 22))
        self.labelLogin.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.labelLogin)

        self.password = QLineEdit()
        self.password.setFont(QFont("times new roman", 22))
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setStyleSheet("background-color: white")
        vbox_master.addWidget(self.password)

        self.labelLogin2 = QLabel()
        self.labelLogin2.setFont(QFont("times new roman", 16))
        self.labelLogin2.setStyleSheet("color:red;")
        self.labelLogin2.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.labelLogin2)

        self.submitPassword = QPushButton("SUBMIT")
        self.submitPassword.setFont(QFont("times new roman", 22))
        self.submitPassword.setFixedWidth(222)
        self.submitPassword.setStyleSheet("background-color: springgreen; border-radius: 15px;")
        self.submitPassword.pressed.connect(self.checkpassword)
        # self.submitPassword.released.connect(self.settings_dialog3.close)
        hbox = QHBoxLayout()
        hbox.addWidget(self.submitPassword)
        vbox_master.addLayout(hbox)

        self.settings_dialog3.setLayout(vbox_master)
        self.settings_dialog3.exec_()

    def checkpassword(self):
        global permission
        fhand = open("Payment and Finances/Staff/DONOT delete this It is a system file.js", 'r')

        actual_password = fhand.readlines()[0].strip()
        entered_password = self.password.text().strip()
        if actual_password == entered_password:
            permission = True
            self.settings_dialog3.close()
        elif actual_password != entered_password:
            permission = False
            self.labelLogin2.setText(" ")
            time.sleep(0.5)
            self.labelLogin2.setText("INCORRECT  PASSWORD\n\nPlease Try Again")



        print("Entered Password :\t", entered_password)

        print("Actual Password :\t", actual_password)

    def changePassword(self):
        self.settings_dialog3 = QDialog()
        self.settings_dialog3.setModal(True)
        self.settings_dialog3.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog3.setWindowTitle("        change Password")
        self.settings_dialog3.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog3.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.labelLogin = QLabel("ENTER PASSWORD")
        self.labelLogin.setFont(QFont("times new roman", 22))
        self.labelLogin.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.labelLogin)

        self.password = QLineEdit()
        self.password.setFont(QFont("times new roman", 22))
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setStyleSheet("background-color: white")
        vbox_master.addWidget(self.password)

        self.labelLogin2 = QLabel()
        self.labelLogin2.setFont(QFont("times new roman", 16))
        self.labelLogin2.setStyleSheet("color:red;")
        self.labelLogin2.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.labelLogin2)

        self.labelLogin3 = QLabel("ENTER PASSWORD")
        self.labelLogin3.setFont(QFont("times new roman", 22))
        self.labelLogin3.setAlignment(Qt.AlignCenter)
        vbox_master.addWidget(self.labelLogin3)

        self.passwordnew = QLineEdit()
        self.passwordnew.setFont(QFont("times new roman", 22))
        self.passwordnew.setAlignment(Qt.AlignCenter)
        self.passwordnew.setStyleSheet("background-color: white")
        vbox_master.addWidget(self.passwordnew)

        self.submitPassword = QPushButton("SUBMIT")
        self.submitPassword.setFont(QFont("times new roman", 22))
        self.submitPassword.setFixedWidth(222)
        self.submitPassword.setStyleSheet("background-color: springgreen; border-radius: 15px;")
        self.submitPassword.pressed.connect(self.savepassword)
        # self.submitPassword.released.connect(self.settings_dialog3.close)
        hbox = QHBoxLayout()
        hbox.addWidget(self.submitPassword)
        vbox_master.addLayout(hbox)

        self.settings_dialog3.setLayout(vbox_master)
        self.settings_dialog3.exec_()

    def savepassword(self):
        global permission
        fhand = open("Payment and Finances/Staff/DONOT delete this It is a system file.js", 'r')

        newPassword = self.passwordnew.text().strip()

        actual_password = fhand.readlines()[0].strip()
        entered_password = self.password.text().strip()
        if actual_password == entered_password:

            fhand.close()
            fhand2 = open("Payment and Finances/Staff/DONOT delete this It is a system file.js", 'w')
            fhand2.write(newPassword)
            self.settings_dialog3.close()
        elif actual_password != entered_password:

            self.labelLogin2.setText(" ")
            time.sleep(0.5)
            self.labelLogin2.setText("INCORRECT  PASSWORD\n\nPlease Try Again")



        print("Entered Password :\t", entered_password)

        print("Actual Password :\t", actual_password)



# GUI window setup clauses

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())









'''
self.settings_dialog = QDialog()
        self.settings_dialog.setModal(True)
        self.settings_dialog.setStyleSheet("background-color:#84eefa; border-radius: 1cm;")
        self.settings_dialog.setWindowTitle("Change Image")
        self.settings_dialog.setWindowIcon(QIcon("School Management Icons/university_library.ico"))
        self.settings_dialog.setGeometry(327, 156, 700, 200)

        vbox_master = QVBoxLayout()

        self.settings_dialog.setLayout(vbox_master)
        self.settings_dialog.exec_()'''