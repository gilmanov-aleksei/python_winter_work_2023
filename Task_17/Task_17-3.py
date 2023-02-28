#! /usr/bin/python

# Создайте класс Shape, объекты которого имеют атрибуты Colour -
# строка, например, "Красный", "Синий"; Square - площадь объекта
# Создайте несколько методов:
# 1. Установить цвет объекта
# 2. Запросить цвет объекта и напечатать его
# 3. Задать площадь объекта
# 4. Запросить площадь объекта

class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def info(self):  # Печатаем информацию об объекте и его площадь
        print(f'Цвет объекта: {self.colour}. Его площадь: {self.square} кв.мм')

    def set_color(self, newcolor):
        self.color = newcolor
    def instal_colour(self):  # Устанвливаем (меняем) цвет объекта
        if self.colour == 'Blue':
            self.colour = 'Red'
        elif self.colour == 'Red':
            self.colour = 'Green'
        else:
            self.colour = 'Blue'

    def get_colour_print(self):  # Запрашиваем цвет объекта и выводим на печать
        obj_colour = self.colour
        print(obj_colour)

    def instal_square(self):  # Устанавливаем новое знавение площади
        self.square += 150

    def get_square(self):  # Запрашиваем площадь объекта и выводим на печать
        obj_square = self.square
        print(obj_square)


b = Shape('Blue', 100)
r = Shape('Red', 200)

b.info()
r.info()

b.instal_colour()
r.instal_colour()

b.get_colour_print()
r.get_colour_print()

b.instal_square()
r.instal_square()

b.get_square()
r.get_square()

b.info()
r.info()
