#! /usr/bin/python

# v1 string
# s = str(input("Введите генетический код: "))
s = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
# Вывод на экран исходной строки
print(s)
# Поиск в строке АГ и замена на ГА
s = s.replace('АГ', 'ГА')
# Поиск в строке ЦТ и замена на ЦАГТ
s = s.replace('ЦТ', 'ЦАГТ')
# Вывод на экран изменённой строки
print(s)