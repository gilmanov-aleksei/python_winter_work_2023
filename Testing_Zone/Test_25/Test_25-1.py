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
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked())
        button.clicked.connect(self.the_button_was_clicked())
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        self.count += 1
        print(f"Clicked! {self.count}")
        self.setWindowTitle(f"Clicked! {self.count}")

    def the_button_was_toggled(self, checked):
        print("Checket?", checked)


app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()
