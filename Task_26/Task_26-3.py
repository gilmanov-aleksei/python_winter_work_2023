#! /usr/bin/python

# Задача 26-3

# Создайте графическое приложение с пунктами меню: Описание, Инструкция, Помощь.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Меню")

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
        self.action_description.triggered.connect(self.description)
        self.action_instruction.triggered.connect(self.instruction)
        self.action_help.triggered.connect(self.help)
        self.action_exit.triggered.connect(self.exit)

    def description(self):
        print("Отображается описание программы")

    def instruction(self):
        print("Отображается инструкция по использованию программы")

    def help(self):
        print("Отображается помощь по программе")

    def exit(self):
        print("Выход")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
