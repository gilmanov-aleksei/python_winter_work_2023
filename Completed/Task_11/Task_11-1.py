#! /usr/bin/python

# Задача 11-1
# - Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# - Напечатайте список дат в 2023 году, когда вход бесплатен.

import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru')

print('Эрмитаж, бесплатные дни на 2023 год')

year = 2023
# Цикл на 12 месяцев
for month in range(1, 13):
    # Счётчик четвергов
    c = 0
    # Цикл по количеству дней в месяце
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        # Проверяем, день недели, если это четверг,
        if calendar.weekday(year, month, day) == 3:
            # то прибавляем счётчик на 1, нет, возврат в  цикл.
            c += 1
            # Прверяем, счётчик равен 3,
            if c == 3:
                # если да, то выводим на экран, день и месяц, возврат в  цикл.
                print(datetime.date(year, month, day).strftime("%d %b"), end='. ')
