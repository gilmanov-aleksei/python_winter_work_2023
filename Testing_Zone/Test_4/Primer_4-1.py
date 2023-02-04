#! /usr/bin/python

# s = str(input("Введите генетический код: "))
s = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
r = [('АГ', 'ГА'), ('ЦТ', 'ЦАГТ')]
# Вывод на экран исходной строки
print(s)
for i in r:
    s = s.replace(*i)
print(s)

s = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
r = [('АГ', 'ГА'), ('ЦТ', 'ЦАГТ')]
mrep = lambda s, d: s if not d else mrep(s.replace(*d.pop()), d)
print(type(mrep))
print(mrep(s, r))
