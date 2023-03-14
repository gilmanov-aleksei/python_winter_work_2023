#! /usr/bin/python

# Задача 22-3
# В Python существуют ключевые слова,
# которые нельзя использовать для названия переменных,
# функций и классов. Для получения списка ключевых слов можно
# воспользоваться атрибутом kwlist из модуля keyword.

# Приведенный ниже код:

# import keyword
# print(keyword.kwlist)
# выодит:

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>


import keyword
import re


def replace_words(text):
    # Получаем список всех ключевых слов Python
    words = keyword.kwlist
    # Создаем регулярное выражение, которое будет находить целые слова
    pattern = r'\b(' + '|'.join(words) + r')\b'
    # Заменяем все целые слова в тексте на '<kw>'
    replaced_text = re.sub(pattern, '<kw>', text)
    return replaced_text


text = 'if x == 2: and  as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))
