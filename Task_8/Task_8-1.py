#! /usr/bin/python

# s1 = str(input("Введите генетический код: "))
s1 = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
# Поиск в строке АГ и замена на ГА
s2 = s1.replace('АГ', 'ГА')
# Поиск в строке ЦТ и замена на ЦАГТ
s3 = s2.replace('ЦТ', 'ЦАГТ')
# Выводна экран исходной строки
print(s1)
# Выводна экран изменённой строки
print(s3)