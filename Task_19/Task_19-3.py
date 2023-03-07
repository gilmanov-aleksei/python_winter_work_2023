#! /usr/bin/python

# Задача 19-3
# Определите класс Person. При создании объекта
# p = Person('Иванов', 'Михаил', 'Федорович')
# необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, first_name, last_name, middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __str__(self):
        return self.middle_name[::-1] + self.last_name[::-1] + self.first_name[::-1]

p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
