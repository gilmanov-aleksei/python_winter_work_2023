#! /usr/bin/python

# Напишите программу, которая считывает информацию из таблицы
# book и формирует DataFrame, полностью соотвествующей этой
# таблице.
# Нарисуйте график колличества книги цен.
# Подсказка: используйте matplotlib и функцию df.plot()

# Программа не готова.

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="12345678",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()

# cur.execute("INSERT INTO pupil VALUES (2, 'Вася', 1)")
# cur.execute('SELECT * FROM pupil')
# d = {'id': [], 'name': [], 'result': []}
# for i in cur.fetchall():
#     print(i)
#     d['id'].append(i[0])
#     d['name'].append(i[1])
#     d['result'].append(i[2])
# # con.commit()
# con.close()

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
