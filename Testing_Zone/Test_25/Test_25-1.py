#! /usr/bin/python

# from PyQt6.QtWidgets import QApplication, QWidget
# # import sys
#
# app = QApplication([])
# window = QWidget()
# window.show()
# app.exec()

# from PyQt6.QtWidgets import QApplication, QPushButton
# import sys
#
# app = QApplication(sys.argv)
# window = QPushButton("Push Me")
# window.show()
# app.exec()

# from PyQt6.QtWidgets import QApplication, QMainWindow
# import sys
#
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.setWindowTitle("My App")
app = QApplication(sys.argv)
window = MainWindows()
window.show()
app.exec()
