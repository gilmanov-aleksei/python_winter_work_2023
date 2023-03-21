#! /usr/bin/python

# Задача 25-1
# Создайте приложение с горизонтальным расположением виджетов

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()
        self.setLayout(hbox)

        label = QLabel("Введите текст:")
        hbox.addWidget(label)

        line_edit = QLineEdit()
        hbox.addWidget(line_edit)

        button = QPushButton("Отправить")
        hbox.addWidget(button)

        self.setGeometry(100, 100, 500, 300)
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
