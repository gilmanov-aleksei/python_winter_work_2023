#! /usr/bin/python

s = 'АГЦТАГЦТАГЦТ'
d = []
for i in range(len(s) - 3):
    d.append(s[i:i + 2])
for i in range(len(d)):
    if d[i] == 'АГ':
        d[i] = 'ГА'
    elif d[i] == 'ЦТ':
        d[i] = 'ЦАГТ'
print(s)
print(''.join(d))