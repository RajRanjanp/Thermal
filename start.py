# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start_WindowCLkZUN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys
import time
class Start_Window(object):
    def __init__(self, main_window):
        self.MainWindow = main_window
    def setupUi(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName(u"Start_Window")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(720, 10, 291, 111))
        self.start_label = QLabel(self.centralwidget)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setGeometry(QRect(270, 10, 491, 81))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.start_label.setFont(font)
        self.start_label.setTextFormat(Qt.RichText)
        self.start_label.setAlignment(Qt.AlignCenter)
        self.run_button = QPushButton(self.centralwidget)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setGeometry(QRect(750, 300, 241, 101))
        self.run_button.setStyleSheet(u"QPushButton{\n"
"image: url(images/run.png);\n"
"image-position: left center;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;              /* White text */\n"
"border-radius: 20px;       /* Rounded corners */\n"
"font-size: 24px;           /* Text size */\n"
"padding: 10px 20px;        /* Button padding */\n"
"\n"
"}")
        self.home_button = QPushButton(self.centralwidget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(750, 430, 241, 101))
        self.home_button.setStyleSheet(u"QPushButton{\n"
"image: url(images/home.svg);\n"
"image-position: left center;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;              /* White text */\n"
"border-radius: 20px;       /* Rounded corners */\n"
"font-size: 24px;           /* Text size */\n"
"padding: 10px 20px;        /* Button padding */\n"
"\n"
"}")
        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(130, 490, 521, 61))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(32)
        self.info.setFont(font1)
        self.timer_lcd = QLCDNumber(self.centralwidget)
        self.timer_lcd.setObjectName(u"timer_lcd")
        self.timer_lcd.setGeometry(QRect(130, 240, 571, 211))
        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")
        self.label_timer.setGeometry(QRect(130, 190, 521, 61))
        self.label_timer.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.timer_lcd.show("18:02")
        self.retranslateUi(MainWindow)
        self.home_button.clicked.connect(self.go_home)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def go_home(self):
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Start_Window", u"Start_Window", None))
        self.logo.setText(QCoreApplication.translate("Start_Window", u"<html><head/><body><p><img src=\"images/logo.png\"/></p></body></html>", None))
        self.start_label.setText(QCoreApplication.translate("Start_Window", u"                                                                                                                                                      START", None))
        self.run_button.setText(QCoreApplication.translate("Start_Window", u"           RUN", None))
        self.home_button.setText(QCoreApplication.translate("Start_Window", u"          HOME", None))
        self.info.setText(QCoreApplication.translate("Start_Window", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; text-decoration: underline;\">Make sure to configure in settings before pressing RUN.</span></p></body></html>", None))
        self.label_timer.setText(QCoreApplication.translate("Start_Window", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Time Remaining:</span></p></body></html>", None))
    # retranslateUi

