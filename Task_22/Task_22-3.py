#! /usr/bin/python

# Задача 22-3
# В Python существуют ключевые слова, которые нельзя использовать для названия
# переменных, функций и классов. Для получения списка ключевых слов можно
# воспользоваться атрибутом kwlist из модуля keyword.
# Приведенный ниже код:

# import keyword
# print(keyword.kwlist)
# выодит:

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Напишите программу, которая принимаетстроку текстаи заменяет в ней всеключевые слова <kw>

# import keyword
# print(keyword.kwlist)