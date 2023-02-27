#! /usr/bin/python

# Задача 16-2
# Вводится двухзначное число, например: 45.
# Напишите такой шаблон, чтобы функция re.findall находила только
# те положительные целые числа, которые не больше, чем это введенное число.
# Т.е. для 45 она находила бы 0, 1 , 12 , 45, но не 46, 100, 1000

import re

# num = input("Введите двухзначное число: ")
numbers = "-25, -15, -10, -5, 0, 1, 5, 8, 12, 25, 31, 43, 56, 62, 74, 87, 91, 100, 1000"
# print(re.findall(r"[-+]\d*", numbers))
print(re.findall('[^-]+?\d.', numbers))
# print(re.findall('\(([^)]+\(?)*[^(]+\)', numbers))
