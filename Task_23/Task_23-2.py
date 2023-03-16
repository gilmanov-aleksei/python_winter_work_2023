#! /usr/bin/python

# Напишите программу, которая считывает информацию из таблицы
# book и формирует DataFrame, полностью соотвествующей этой
# таблице.
# Нарисуйте график колличества книги цен.
# Подсказка: используйте matplotlib и функцию df.plot()

# Программа не начата и не готова.

import psycopg2
import pandas as ps
import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [3, 6, 1, 8, 2]

# Создаем ось и добавляем данные на график
plt.plot(x, y)

# Добавляем подписи осей и заголовок
plt.xlabel('Books')
plt.ylabel('Price')
plt.title('Books and Price')

# Отображаем график
plt.show()
