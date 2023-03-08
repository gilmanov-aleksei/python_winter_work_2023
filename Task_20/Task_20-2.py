#! /usr/bin/python

# Задача 20-2
# Напишите функцию, которая на вход получает DataFrame,
# который содержит числа и строки,
# а в качестве результата возвращает сумму всех чисел.

import pandas as pd


def sum_numbers(df):
    num = df.select_dtypes(include='number').columns
    return df[num].sum().sum()


df = pd.DataFrame(
    [[8, 'abc', 5, 'cba', 3],
     [2, 'def', 3, 'fed', 7],
     [9, 'xyz', 4, 'zyx', 2]],
    columns=['A', 'B', 'C', 'D', 'E'])

print(sum_numbers(df))
print(df)

#
# import pandas as pd
#
#
# def sum_num(df1, axis=0):
#     num = df1.select_dtypes(include=['number']).columns
#     return df1[num].sum(axis=axis).sum()
#
#
# df1 = pd.DataFrame(
#     [[8, 'abc', 5, 'cba', 3],
#      [2, 'def', 3, 'fed', 7],
#      [9, 'xyz', 4, 'zyx', 2]],
#     columns=['A', 'B', 'C', 'D', 'E'])
#
# print(df1)
#
# # Сумма значений по колонкам
# # сумма по столбцам
# print(df1.sum())
# # Сумма значений по строкам
# # сумма по строкам
# print(df1.sum(axis=1))
# # Сумма значений по всей таблице
# # сумма по строкам и столбцам
# print(df1.sum(axis=0).sum(axis=0))
