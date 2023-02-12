#! /usr/bin/python

# Задача 11-3
#  - Напишите функцию, которая переводит арабские числа в римские.
#  - Например : 2023 -->MMXXIII

def enter_num():
    print('Перевод цифр, арабские в римские')
    while True:
        a = input('Введите число от 1 до 3999, 0 - выход: ')
        if a == '0':
            break
        elif not a.isdigit():
            print("Вы ввели не число, повторите ввод")
        elif a > '3999':
            print("Вы ввели число больше 3999, повторите ввод")
        else:
            return a


def checkio1(data):
    base = "I" * data

    base = base.replace("I" * 5, "V")
    base = base.replace("V" * 2, "X")
    base = base.replace("X" * 5, "L")
    base = base.replace("L" * 2, "C")
    base = base.replace("C" * 5, "D")
    base = base.replace("D" * 2, "M")

    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")

    return base


def checkio2(data):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]

    return t + h + te + o


def checkio3(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result


d = {}
num = enter_num()
if num is None:
    print("Выход")
else:
    print(checkio1(int(num)))
    print(checkio2(int(num)))
    print(checkio3(int(num)))
