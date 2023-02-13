#! /usr/bin/python

# Задача 11-1
# - Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# - Напечатайте список дат в 2023 году, когда вход бесплатен.

import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru')

def enter_year():
    print('Хотите узнать когда в Эрмитаже бесплатные дни?')
    # Бесконечный цикл
    while True:
        # Запрос года от пользователя
        y = input('Введите год, 0 - выход: ')
        # Проверка ввода, если ноль,
        if y == '0':
            #  то выход из функции
            break
        # Проверяем, если это не число, то повторяем цикл
        elif not y.isdigit():
            print("Вы не ввели год, повторите ввод")
        # проеряем число, если оно больше 3999, то повторяем цикл
        elif y < '1762':
            print("Эрмитаж ещё не был построен, повторите ввод")
        elif y > '2999':
            print("Это далёкое будущие, повторите ввод")
        else:
            # Выход из функции с числом которое ввел пользователь
            return int(y)


def free_day_ermitazh(e_year):
    pass

#
# for month in range(1, 13):
#     for day in range(1, calendar.monthrange(e_year, month)[1] + 1):
#         dd = calendar.weekday(e_year, month, day)
# return


# # В переменную записываем функцию ввода года от пользователя
# year = enter_year()
# # Проеряем полученное значение от пользователя,
# if year is None:
#     # если значения нет, то печатаем Выход
#     # и завершаем программу
#     print("Выход")
# # Иначе выводим результат функции
# # бесплатные дни в Эрмитаже
# else:
#     print(free_day_ermitazh(year))

date = datetime.date.today()
weekday = datetime.date.today().weekday()
count_mounth = calendar.weekday(date.year, date.month, 1)
print(weekday)
# print(datetime.datetime.strptime(str(weekday), '%B'))
print(date)
print(count_mounth)
print(f'Сегодня {str(date.day)} день месяца!!!')
today = datetime.datetime.now()
print(datetime.datetime.strftime(today, '%d %B'))