#! /usr/bin/python

# v4 lambda
# s = str(input("Введите генетический код: "))
s = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
# Вывод на экран исходной строки
print(s)
# Список для поиска и замены букв
r = [('ЦТ', 'ЦАГТ'), ('АГ', 'ГА')]
print(type(r))
# Функция по поиску и замены букв.
# Берёт последние значение из списка,
# записывает его в функцию с распаковкой,
# и удаляет его из кортежа.
rep = lambda s, d: s if not d else rep(s.replace(*d.pop()), d)
# Вывод на экран изменённой строки
print(rep(s, r))