#! /usr/bin/python

# Задача 11-3
#  - Напишите функцию, которая переводит арабские числа в римские.
#  - Например : 2023 -->MMXXIII

# Функция запрос ввода числа от пользователя
def enter_num():
    print('Перевод цифр, арабские в римские')
    # Бесконечный цикл
    while True:
        # Запрос ввода числа от пользователя
        a = input('Введите число от 1 до 3999, 0 - выход: ')
        # Проверка ввода, если ноль,
        if a == '0':
            #  то выход из функции
            break
        # Проверяем, если это не число, то повторяем цикл
        elif not a.isdigit():
            print("Вы ввели не число, повторите ввод")
        # проеряем число, если оно больше 3999, то повторяем цикл
        elif a > '3999':
            print("Вы ввели число больше 3999, повторите ввод")
        else:
            # Выход из функции с числом которое ввел пользователь
            return a


# Функция перевода числа из арабских цифр в римские
def arab_to_rome(atr):
    # Словарь едениц
    units = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    # Словарь дестяков
    dozens = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    # Словарь сотен
    hundreds = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    # Словарь тысяч
    thousands = {0: "", 1: "M", 2: "MM", 3: "MMM"}

    # Делим на тысячу без остатка,
    # результат будет ключом в словаре,
    # записываем значение в переменную тысячи
    t = thousands[atr // 1000]
    # Делим на сто без остатка, потом делим на десять,
    # остаток будет ключом в словаре,
    # записываем значение в переменную сотни
    h = hundreds[atr // 100 % 10]
    # Делим на десять без остатка, потом делим на десять,
    # остаток будет ключом в словаре,
    # записываем значение в переменную десятки
    d = dozens[atr // 10 % 10]
    # Делим на десять, остаток будет ключом в словаре,
    # записываем значение в переменную еденицы
    u = units[atr % 10]
    # Результат, складываем полученные буквы вмести
    return t + h + d + u


# В переменную записываем функцию ввода числа от пользователя
num = enter_num()
# Проеряем полученное значение от пользователя,
if num is None:
    # если значения нет, то печатаем Выход
    # и завершаем программу
    print("Выход")
# Иначе печатем результат функции
# перевода числа из арбских чисел в римские
else:
    print(arab_to_rome(int(num)))
