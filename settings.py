# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window_Thermal_Chamber - CopySQBpsm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLCDNumber, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Settings_Window(object):
    def __init__(self, main_window):
        self.MainWindow = main_window
    def setupUi(self):
        MainWindow = self.MainWindow
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"Settings_Window")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(720, 10, 291, 111))
        self.label_settings = QLabel(self.centralwidget)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setGeometry(QRect(270, 10, 491, 81))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label_settings.setFont(font)
        self.label_settings.setTextFormat(Qt.RichText)
        self.label_settings.setAlignment(Qt.AlignCenter)
        self.label_fan = QLabel(self.centralwidget)
        self.label_fan.setObjectName(u"label")
        self.label_fan.setGeometry(QRect(90, 300, 331, 61))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(32)
        self.label_fan.setFont(font1)
        self.label_temperature = QLabel(self.centralwidget)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setGeometry(QRect(80, 140, 381, 61))
        self.label_temperature.setFont(font1)
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(410, 250, 231, 171))
        self.dial.setMinimum(0)  # Minimum value of the dial
        self.dial.setMaximum(100)  # Maximum value of the dial
        self.dial.setValue(0)
        self.dial.setStyleSheet(u"QDial {\n"
"	color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));\n"
"    background-color: #f0f0f0; /* Dial background */\n"
"    border: 2px solid #3b3b3b; /* Border around the dial */\n"
"    border-radius: 20px;\n"
"}")
        self.temperature_radio_60 = QRadioButton(self.centralwidget)
        self.temperature_radio_60.setObjectName(u"radioButton")
        self.temperature_radio_60.setGeometry(QRect(540, 130, 151, 91))
        self.temperature_radio_60.setStyleSheet(u"QRadioButton {\n"
"    font-size: 30px;  /* Increase font size to make text larger */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;  /* Set the width of the radio button circle */\n"
"    height: 30px; /* Set the height of the radio button circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4CAF50;  /* Green color when checked */\n"
"    border: 2px solid #4CAF50;  /* Border color */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: white;  /* White background when unchecked */\n"
"    border: 2px solid #888;  /* Gray border when unchecked */\n"
"}\n"
"")
        self.temperature_radio_40 = QRadioButton(self.centralwidget)
        self.temperature_radio_40.setObjectName(u"temperature_radio_40")
        self.temperature_radio_40.setGeometry(QRect(760, 130, 151, 91))
        self.temperature_radio_40.setStyleSheet(u"QRadioButton {\n"
"    font-size: 30px;  /* Increase font size to make text larger */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;  /* Set the width of the radio button circle */\n"
"    height: 30px; /* Set the height of the radio button circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4CAF50;  /* Green color when checked */\n"
"    border: 2px solid #4CAF50;  /* Border color */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: white;  /* White background when unchecked */\n"
"    border: 2px solid #888;  /* Gray border when unchecked */\n"
"}\n"
"")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(730, 300, 241, 101))
        self.save_button.setStyleSheet(u"QPushButton{\n"
"image: url(images/save.svg);\n"
"image-position: left center;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;              /* White text */\n"
"border-radius: 20px;       /* Rounded corners */\n"
"font-size: 24px;           /* Text size */\n"
"padding: 10px 20px;        /* Button padding */\n"
"\n"
"}")
        self.home_button_ = QPushButton(self.centralwidget)
        self.home_button_.setObjectName(u"home_button_")
        self.home_button_.setGeometry(QRect(730, 430, 241, 101))
        self.home_button_.setStyleSheet(u"QPushButton{\n"
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
        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(160, 490, 521, 61))
        self.label_info.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.home_button_.clicked.connect(self.go_home)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def go_home(self):
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Settings_Window", u"Settings_Window", None))
        self.logo.setText(QCoreApplication.translate("Settings_Window", u"<html><head/><body><p><img src=\"images\logo.png\"/></p></body></html>", None))
        self.label_settings.setText(QCoreApplication.translate("Settings_Window", u"                                                                                                                                                      SETTINGS", None))
        self.label_fan.setText(QCoreApplication.translate("Settings_Window", u"Fan Speed:", None))
        self.label_temperature.setText(QCoreApplication.translate("Settings_Window", u"Set Temperature:", None))
        self.temperature_radio_60.setText(QCoreApplication.translate("Settings_Window", u"60\u00b0C", None))
        self.temperature_radio_40.setText(QCoreApplication.translate("Settings_Window", u"-40\u00b0C", None))
        self.save_button.setText(QCoreApplication.translate("Settings_Window", u"    SAVE", None))
        self.home_button_.setText(QCoreApplication.translate("Settings_Window", u"    HOME", None))
        self.label_info.setText(QCoreApplication.translate("Settings_Window", u"<html><head/><body><p><span style=\" font-size:16pt; font-style:italic; text-decoration: underline;\">Press save to apply your changes.</span></p></body></html>", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Settings_Window(None)
    ui.setupUi()
    
    # Store the reference to the main window in the UI
    ui.MainWindow = MainWindow  # Make sure the MainWindow reference is available in the UI

    MainWindow.show()
    sys.exit(app.exec_())