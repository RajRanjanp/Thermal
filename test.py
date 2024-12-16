from Main_window import *
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import time
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Home_Window()
ui.setupUi(MainWindow)
    
    # Store the reference to the main window in the UI
ui.MainWindow = MainWindow  # Make sure the MainWindow reference is available in the UI

MainWindow.show()
print(time.time())
sys.exit(app.exec_())