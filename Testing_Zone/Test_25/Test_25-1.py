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
#
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys
#
# class MainWindows(QMainWindow):
#     def __init__(self):
#         super(MainWindows, self).__init__()
#         self.setWindowTitle("Hello world")
#         self.resize(400, 400)
#         # self.setWindowOpacity(0.1)
#         self.move(50, 50)
# app = QApplication(sys.argv)
# window = MainWindows()
# window.show()
# app.exec()

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        print(button.text())
        button.setCheckable(True)

        # self.change_text(button)
        print(button.text())
        button.clicked.connect(self.the_button_was_clicked())
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)
window = MainWindows()
window.show()
app.exec()
