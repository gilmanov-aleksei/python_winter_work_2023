#! /usr/bin/python

# Задача 25-1
# Создайте приложение с горизонтальным расположением виджетов

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Горизонтальное расположение виджетов")
        self.setGeometry(100, 100, 400, 200)

        # создание горизонтального слоя
        h_box = QHBoxLayout()

        # создание виджетов
        label = QLabel("Имя:")
        line_edit = QLineEdit()
        button = QPushButton("Нажми меня")

        # добавление виджетов в горизонтальный слой
        h_box.addWidget(label)
        h_box.addWidget(line_edit)
        h_box.addWidget(button)

        # установка слоя на окно
        self.setLayout(h_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
