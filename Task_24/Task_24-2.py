#! /usr/bin/python

# Задача 24-2
# Создайте запрос, который находит авторов, у которых только
# минимальное количество книг на складе (в таблице book).
# Используйте для этого View.

# Программа не закончена

import psycopg2

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
# rows = cur.fetchall()
# print(rows)
# Добавляем названия колонок для DataFrame

cur.close()
con.close()