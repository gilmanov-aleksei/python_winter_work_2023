#! /usr/bin/python

# Задача 26-3

# Создайте графическое приложение с пунктами меню: Описание, Инструкция, Помощь.
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Меню")
        self.setGeometry(100, 100, 350, 250)

        # Создаем QLabel для вывода текста
        self.label = QLabel(self)
        self.label.setGeometry(20, 30, 300, 200)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Создаем пункты меню
        self.action_description = QAction("&Описание", self)
        self.action_instruction = QAction("&Инструкция", self)
        self.action_help = QAction("&Помощь", self)
        self.action_exit = QAction("&Выход", self)

        # Добавляем пункты в меню
        self.menu_bar = self.menuBar()
        self.menu = self.menu_bar.addMenu("&Меню")
        self.menu.addAction(self.action_description)
        self.menu.addAction(self.action_instruction)
        self.menu.addAction(self.action_help)
        self.menu.addAction(self.action_exit)

        # Назначаем обработчик событий для каждого пункта меню
        self.action_description.triggered.connect(self.on_description)
        self.action_instruction.triggered.connect(self.on_instruction)
        self.action_help.triggered.connect(self.on_help)
        self.action_exit.triggered.connect(self.close)

    def on_description(self):
        self.label.setText("Описание программы\n\n"
                           "Демонстрация работы программы\n"
                           "на Python с модулем PyQt6")

    def on_instruction(self):
        self.label.setText("Инструкция по программе\n\n"
                           "Используя мышку, нажимайте на кнопку Меню\n")

    def on_help(self):
        self.label.setText("Помощь по программе\n\n"
                           "Смотри инструкцию по программе\n"
                           "Используя мышку, нажимайте на кнопку Меню\n")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
