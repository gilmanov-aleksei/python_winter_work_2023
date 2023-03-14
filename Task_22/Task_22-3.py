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


def replace_words(text):
    # Получаем список всех ключевых слов Python
    kw_list = keyword.kwlist
    # Создаем словарь, где ключи - это ключевые слова, а значения - это '<kw>'
    kw_replace = {kw: '<kw>' for kw in kw_list}
    # Разбиваем текст на отдельные слова
    words = text.split()
    # Заменяем все ключевые слова в тексте на '<kw>'
    for i in range(len(words)):
        if words[i] in kw_replace:
            words[i] = kw_replace[words[i]]
    # Склеиваем слова обратно в строку
    new_text = ' '.join(words)
    return new_text


text = 'if x == 2: and  as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))
