#! /usr/bin/python

# Задача 21-3
# Создайте таблицу book с полями book_id(int), book_title(text),
# book_author(text), publisher_id(int)
# Введите несколько книг нескольких авторов.
# Сделайте несколько SELECT для выборки книг по авторам, по названиям.

# CREATE TABLE book (
#   book_id serial PRIMARY KEY,
#   book_title text,
#   book_author text,
#   publisher_id integer
# );

# INSERT INTO book (book_title, book_author, publisher_id) VALUES
#     ('Евгений Онегин', 'Александр Пушкин', 1),
#     ('Мастер и Маргарита', 'Михаил Булгаков', 2),
#     ('Изучаем Python', 'Марка Лутца', 3);
#     ('Основы Python', 'Аллен Дауни', 4),
#     ('Нравственные письма к Луцилию', 'Сенека Луций Анней', 5),
#     ('Суждения и беседы', 'Конфуций', 6);

# SELECT * FROM book WHERE book_author = 'Александр Пушкин';
# SELECT * FROM book WHERE book_title = 'Изучаем Python';
