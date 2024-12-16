# Monitor.py
import sys
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLCDNumber, QWidget
from PyQt5.QtGui import QFont
from Plot_data import Plot_data

class Monitor_Window(object):
    def __init__(self, main_window):
        self.MainWindow = main_window  # Store the MainWindow reference

    def setupUi(self):
        # Use the reference to the MainWindow passed during initialization
        MainWindow = self.MainWindow
        MainWindow.setObjectName("Monitor_Window")
        MainWindow.resize(1024, 600)

        # Central widget setup
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # PLOT Button
        self.plot_button = QPushButton(self.centralwidget)
        self.plot_button.setObjectName("plot_button")
        self.plot_button.setGeometry(QRect(800, 410, 141, 51))
        self.plot_button.setText("   PLOT")
        self.plot_button.setStyleSheet("""
            QPushButton {
                image: url(images/home.svg);
                image-position: left center;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));
                color: white;
                border-radius: 20px;
                font-size: 24px;
                padding: 10px 20px;
            }
        """)

        # HOME Button
        self.home_button = QPushButton(self.centralwidget)
        self.home_button.setObjectName("pushButton_6")
        self.home_button.setGeometry(QRect(800, 480, 141, 51))
        self.home_button.setText("    HOME")
        self.home_button.setStyleSheet("""
            QPushButton {
                image: url(images/home.svg);
                image-position: left center;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(135, 206, 235, 255), stop:1 rgba(173, 216, 230, 255));
                color: white;
                border-radius: 20px;
                font-size: 24px;
                padding: 10px 20px;
            }
        """)

        # Labels and LCDs
        self.monitor_label = QLabel(self.centralwidget)
        self.monitor_label.setObjectName("label_5")
        self.monitor_label.setGeometry(200, 10, 491, 81)
        self.monitor_label.setText("Monitor")
        self.monitor_label.setAlignment(Qt.AlignCenter)
        self.monitor_label.setFont(QFont("Times New Roman", 35, QFont.Bold))

        self.temperature_label = QLabel(self.centralwidget)
        self.temperature_label.setObjectName("temperature_label")
        self.temperature_label.setGeometry(90, 130, 331, 61)
        self.temperature_label.setText("Temperature (°C)")
        self.temperature_label.setFont(QFont("Times New Roman", 30))

        self.lcd_temperature = QLCDNumber(self.centralwidget)
        self.lcd_temperature.setObjectName("lcdNumber_1")
        self.lcd_temperature.setGeometry(400, 120, 281, 91)

        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName("pressure_label")
        self.pressure_label.setGeometry(90, 270, 331, 61)
        self.pressure_label.setText("Pressure (bar)")
        self.pressure_label.setFont(QFont("Times New Roman", 30))

        self.lcd_pressure = QLCDNumber(self.centralwidget)
        self.lcd_pressure.setObjectName("lcdNumber_2")
        self.lcd_pressure.setGeometry(400, 260, 281, 91)

        self.humidity_label = QLabel(self.centralwidget)
        self.humidity_label.setObjectName("humidity_label")
        self.humidity_label.setGeometry(90, 420, 331, 61)
        self.humidity_label.setText("Humidity (% RH)")
        self.humidity_label.setFont(QFont("Times New Roman", 30))

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QRect(710, 10, 291, 111))

        self.lcd_humidity = QLCDNumber(self.centralwidget)
        self.lcd_humidity.setObjectName("lcdNumber_3")
        self.lcd_humidity.setGeometry(400, 410, 281, 91)
        self.lcd_humidity.display("50")

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar and status bar setup
        self.menubar = MainWindow.menuBar()
        self.statusbar = MainWindow.statusBar()

        # Call retranslateUi to update text
        self.retranslateUi(MainWindow)

        # Connect buttons to their slots
        self.home_button.clicked.connect(self.go_home)
        self.plot_button.clicked.connect(self.plot_data)

        QMetaObject.connectSlotsByName(MainWindow)

    def plot_data(self):
        # Create and display the plot window
        self.plot_window = QMainWindow()
        self.plot_ui = Plot_data(self.plot_window,self.MainWindow)  # Pass MainWindow to Plot_data
        self.plot_ui.setupUi()  # Set up the plot window UI
        self.plot_window.show()  # Show the plot window
    def go_home(self):
        self.MainWindow.close()
        # from Main_window import Home_Window
        # main_window = QMainWindow()
        # main_ui = Home_Window()
        # main_ui.setupUi(main_window)
        # main_window.show()

    def retranslateUi(self, MainWindow):
        # Update window title and other UI elements
        MainWindow.setWindowTitle(QCoreApplication.translate("MonitorWindow", "Monitor Window", None))
        self.plot_button.setText(QCoreApplication.translate("MonitorWindow", "   PLOT", None))
        self.home_button.setText(QCoreApplication.translate("MonitorWindow", "    HOME", None))
        self.logo.setText(QCoreApplication.translate("MonitorWindow", '<html><head/><body><p><img src=\"images\logo.png\"/></p></body></html>', None))
        self.monitor_label.setText(QCoreApplication.translate("MonitorWindow", " MONITOR", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Monitor_Window(MainWindow)  # Pass the MainWindow reference here
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())
