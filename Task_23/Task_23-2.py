#! /usr/bin/python

# Напишите программу, которая считывает информацию из таблицы Postgres
# book и формирует DataFrame, полностью соотвествующей этой
# таблице.
# Нарисуйте график колличества книги цен.
# Подсказка: используйте matplotlib и функцию df.plot()

# Программа не готова.

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
# Подключаемся к базе Postgres
con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="12345678",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()
# Вызываем таблицу book
cur.execute('SELECT * FROM book')
# Копируем таблицу из базы Postgres в переменную
rows = cur.fetchall()
# Добавляем названия колонок для DataFrame
cols = ['book_id', 'title', 'price', 'amount', 'author_id']
# Записываем данные в таблицу DataFrame
df = pd.DataFrame(rows, columns=cols)

# Создаем ось и добавляем данные графика
df.plot(x='amount', y='price', kind='bar')
# Добавляем подписи осей и заголовок
plt.title('Books by price')
plt.xlabel('Amount')
plt.ylabel('Price')
# Отображаем график
plt.show()

cur.close()
con.close()
