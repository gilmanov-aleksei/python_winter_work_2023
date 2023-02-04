#! /usr/bin/python

# s = str(input("Введите генетический код: "))
s = 'АГЦТААГГЦЦТТГАГАТЦТТАЦЦТАГТАГЦТ'
r = [('АГ', 'ГА'), ('ЦТ', 'ЦАГТ')]
print(s)
for i in r:
    s = s.replace(i[0], i[1])
print(s)



