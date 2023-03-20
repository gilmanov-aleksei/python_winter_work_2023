#! /usr/bin/python

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindows(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My App")
#         button = QPushButton("Press Me!")
#         # button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         button = self.sender()
#         button.setText("You already clicked me.")
#         button.setEnabled(False)
#         self.setWindowTitle("My Oneshot App")
#
#
# app = QApplication(sys.argv)
# window = MainWindows()
# window.show()
# sys.exit(app.exec())

import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

windows_titles = ['My App', 'My App',
                   'Still My App', 'Still My App',
                   'Whath on earth', 'STOP']
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_windows_title_changed)
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked.")
        new_windows_title = choice(windows_titles)
        button = self.sender()
        button.setText("You already clicked me.")
        print("Seting title: %s" % new_windows_title)
        self.setWindowTitle(new_windows_title)
    def the_windows_title_changed(self, windows_title):
        print("Window title changed: %s" % windows_title)



app = QApplication(sys.argv)
window = MainWindows()
window.show()
sys.exit(app.exec())
