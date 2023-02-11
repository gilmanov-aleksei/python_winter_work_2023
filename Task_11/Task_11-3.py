#! /usr/bin/python

def enter_num():
    print('Перевод цифр, арабские в римские')
    while True:
        a = input('Введите число, 0 - выход: ')
        if a == '0':
            break
        elif not a.isdigit():
            print("Вы ввели не число, повторите ввод")
        elif len(a) > 4:
            print("Вы ввели большое число, повторите ввод")
        else:
            return a


d = {}
n = enter_num()
if n is not None:
    print(n)
else:
    print("Exit")
