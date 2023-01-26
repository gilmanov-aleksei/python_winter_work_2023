#! /usr/bin/python

abc = input('Введите пример: ').split()

a = int(abc[0])
b = int(abc[2])
c = abc[1]
if c == '+':
    print(abc[0], '+', abc[2], '=', a + b)
if c == '-':
    print(abc[0], '-', abc[2], '=', a - b)
if c == '*':
    print(abc[0], '*', abc[2], '=', a * b)
if c == '/':
    if b != 0:
        print(abc[0], '/', abc[2], '=', a / b)
    else:
        print("Деление на ноль!")

