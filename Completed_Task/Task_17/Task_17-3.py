#! /usr/bin/python

# Создайте класс Shape, объекты которого имеют атрибуты Colour -
# строка, например, "Красный", "Синий"; Square - площадь объекта
# Создайте несколько методов:
# 1. Установить цвет объекта
# 2. Запросить цвет объекта и напечатать его
# 3. Задать площадь объекта
# 4. Запросить площадь объекта

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square

    def info(self):  # Печатаем информацию об объекте и его площадь
        print(f'Цвет объекта: {self.color}. Его площадь: {self.square} кв.мм')

    def set_color(self, newcolor):  # Устанавливаем новый цвет объекта
        self.color = newcolor

    def get_color_print(self):  # Запрашиваем цвет объекта и выводим на печать
        obj_colour = self.color
        print(obj_colour)

    def set_square(self, newsquare):  # Увеличиваем площадь объекта
        self.square += newsquare

    def get_square(self):  # Запрашиваем площадь объекта и выводим на печать
        obj_square = self.square
        print(obj_square)


b = Shape('Blue', 100)
r = Shape('Red', 200)

b.info(), r.info()
b.set_color('Red'), r.set_color('Green')
b.get_color_print(), r.get_color_print()
b.set_square(100), r.set_square(150)
b.get_square(), r.get_square()
b.info(), r.info()
