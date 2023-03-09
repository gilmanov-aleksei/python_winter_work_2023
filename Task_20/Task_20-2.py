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
