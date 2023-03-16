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


def replace_words(txt):
    # Получаем список всех ключевых слов Python
    kw_list = keyword.kwlist
    # Создаем словарь, где ключевые слова - это ключи, а значения - это '<kw>'
    kw_replace = {kw: '<kw>' for kw in kw_list}
    # Разбиваем текст на отдельные слова
    words = txt.split()
    new_txt = []
    # Заменяем все ключевые слова в тексте на '<kw>'
    for i in range(len(words)):
        if words[i] in kw_replace:
            new_txt.append(kw_replace[words[i]])
        else:
            new_txt.append(words[i])
    # Собираем слова обратно в строку
    new_txt = ' '.join(new_txt)
    return new_txt


text = 'if x == 2 and as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))
