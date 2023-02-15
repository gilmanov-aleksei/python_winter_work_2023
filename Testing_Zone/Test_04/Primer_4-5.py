#! /usr/bin/python

lst = [('Иваном', 100), ('Петров', 200), ('Лунин', 200), ('Сидоров', 200), ('Воробьев', 100), ('Лунин', 100)]

s = lambda x: (-x[1], x[0]) #tuple(sorted(x[1]))

print(sorted(lst, key=s))