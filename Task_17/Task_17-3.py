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

    def info(self):
        print(f'Цвет объекта: {self.colour}. Его площадь: {self.square} кв.мм')

    def instsl_colour(self):
        if self.colour == 'Blue':
            self.colour = 'Red'
        elif self.colour == 'Red':
            self.colour = 'Green'
        else:
            self.colour = 'Blue'

    def get_colour_print(self):
        obj_colour = self.colour
        print(obj_colour)

    def instal_square(self):
        self.square += 150

    def get_square(self):
        obj_square = self.square
        print(obj_square)


b = Shape('Blue', 100)
r = Shape('Red', 200)

b.info()
r.info()

b.instsl_colour()
r.instsl_colour()

b.get_colour_print()
r.get_colour_print()

b.instal_square()
r.instal_square()

b.get_square()
r.get_square()
