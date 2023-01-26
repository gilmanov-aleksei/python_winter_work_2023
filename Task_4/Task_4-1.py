#! /usr/bin/python

abc = input('Введите пример: ').split()

if abc[1] == '+':
    print(abc[0], '+', abc[2], '=', int(abc[0])+int(abc[2]))
if abc[1] == '-':
    print(abc[0], '-', abc[2], '=', int(abc[0])-int(abc[2]))
if abc[1] == '*':
    print(abc[0], '*', abc[2], '=', int(abc[0])*int(abc[2]))
if abc[1] == '/':
    if int(abc[2]) != 0:
        print(abc[0], '/', abc[2], '=', int(abc[0])/int(abc[2]))
    else:
        print("Деление на ноль!")

