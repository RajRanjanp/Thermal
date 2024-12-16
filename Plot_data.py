# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Monitor_thermal_chamberjSenTq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QMenuBar, QStatusBar, QFrame 
import sys
import pyqtgraph as pg



class Plot_data(object):
    def __init__(self, main_window , monitor_window):
        self.monitor_window = monitor_window
        self.MainWindow = main_window
    def setupUi(self):
        # Resize the MainWindow
        MainWindow = self.MainWindow
        MainWindow.setObjectName("Plot_Window")
        MainWindow.resize(1027, 600)
        
        # Set up the central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # HOME button
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName("back_button")
        self.back_button.setGeometry(850, 450, 141, 51)
        self.back_button.setStyleSheet("""
            QPushButton {
                image: url(home.svg);
                image-position: left center;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));
                color: white;
                border-radius: 20px;
                font-size: 24px;
                padding: 10px 20px;
            }
        """)


        # Label with logo
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName("label_2")
        self.logo.setGeometry(730, 10, 261, 111)

        # Set frame

        # Title label
        self.plot_label = QLabel(self.centralwidget)
        self.plot_label.setObjectName("plot_label")
        self.plot_label.setGeometry(200, 10, 491, 81)
        font = self.plot_label.font()
        font.setFamily("Times New Roman")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.plot_label.setFont(font)
        self.plot_label.setTextFormat(Qt.RichText)
        self.plot_label.setAlignment(Qt.AlignCenter)

        # Set the central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Set up the menubar and statusbar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(0, 0, 1027, 21)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Call retranslateUi to set the translations
        self.retranslateUi(MainWindow)
        self.back_button.clicked.connect(self.go_back)

        # Set up UI components signals and slots
        QMetaObject.connectSlotsByName(MainWindow)
    def go_back(self):
        self.MainWindow.close()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Plot_Window", "Plot_Window", None))
        self.back_button.setText(QCoreApplication.translate("Plot_Window", "    BACK", None))
        self.logo.setText(QCoreApplication.translate("Plot_Window", "<html><head/><body><p><img src=\"images/logo.png\"/></p></body></html>", None))
        self.plot_label.setText(QCoreApplication.translate("Plot_Window", "PLOT", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Create UI object and set up UI
    ui = Plot_data(MainWindow,None)
    ui.setupUi()

    # Show the main window
    MainWindow.show()

    # Run the application
    sys.exit(app.exec_())
