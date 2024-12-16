from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from Monitor import Monitor_Window
from settings import Settings_Window
from start import Start_Window
import sys

class Home_Window(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"Home_Window")
        MainWindow.resize(1024, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Label for the title
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"Thermal Chamber")
        self.label.setGeometry(QRect(10, 10, 991, 81))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        # Start Button
        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"Play Button")
        self.play_button.setGeometry(QRect(90, 130, 291, 131))
        self.play_button.setStyleSheet(u"QPushButton{\n"
"image: url(images/play.svg);\n"
"image-position: left center ;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"padding: 10px 20px;\n"
"}")

        # Monitor Button
        self.monitor_button = QPushButton(self.centralwidget)
        self.monitor_button.setObjectName(u"monitor_button")
        self.monitor_button.setGeometry(QRect(90, 320, 291, 131))
        self.monitor_button.setStyleSheet(u"QPushButton{\n"
"image: url(images/monitor-dashboard.png);\n"
"image-position: left center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"padding: 10px 20px;\n"
"}")

        # Settings Button
        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(420, 130, 311, 131))
        self.settings_button.setStyleSheet(u"QPushButton{\n"
"image-position: left center;\n"
"image: url(images/settings.svg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"padding: 10px 20px;\n"
"}")

        # Shutdown Button
        self.shutdown_button = QPushButton(self.centralwidget)
        self.shutdown_button.setObjectName(u"shutdown_button")
        self.shutdown_button.setGeometry(QRect(420, 320, 311, 131))
        self.shutdown_button.setStyleSheet(u"QPushButton{\n"
"image-position: left center;\n"
"image: url(images/on-off.svg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));\n"
"color: white;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"padding: 10px 20px;\n"
"}")

        # Logo image
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(740, 440, 270, 90))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 0))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Connect the "MONITOR" button to open the monitor window
        self.monitor_button.clicked.connect(self.open_monitor_window)
        self.settings_button.clicked.connect(self.open_settings_window)
        self.play_button.clicked.connect(self.open_start_window)

    def open_monitor_window(self):
        #Create a new window of same dimension
        self.monitor_window = QMainWindow()
        self.monitor_ui = Monitor_Window(self.monitor_window)  # Create the monitor window
        self.monitor_ui.setupUi()  # Setup the monitor UI
        self.monitor_window.show()  # Show the monitor window
        #self.MainWindow.close() 

    def open_settings_window(self):
        #Create a new window of same dimension
        self.settings_window = QMainWindow()
        self.settings_ui = Settings_Window(self.settings_window)  # Create the settings window
        self.settings_ui.setupUi()  # Setup the monitor UI
        self.settings_window.show()  # Show the monitor window
        #self.MainWindow.close()
    
    def open_start_window(self):
        #Create a new window of same dimension
        self.start_window = QMainWindow()
        self.start_ui = Start_Window(self.start_window)  # Create the settings window
        self.start_ui.setupUi()  # Setup the monitor UI
        self.start_window.show()  # Show the monitor window
        #self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Thermal Chamber", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"              START", None))
        self.monitor_button.setText(QCoreApplication.translate("MainWindow", u"              MONITOR", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"              SETTINGS", None))
        self.shutdown_button.setText(QCoreApplication.translate("MainWindow", u"              SHUTDOWN", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"images\logo.png\"/></p></body></html>", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Home_Window()
    ui.setupUi(MainWindow)
    
    # Store the reference to the main window in the UI
    ui.MainWindow = MainWindow  # Make sure the MainWindow reference is available in the UI

    MainWindow.show()
    sys.exit(app.exec_())
