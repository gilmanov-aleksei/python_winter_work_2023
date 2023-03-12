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
#     ('Мастер и Маргарита', 'Михаил Булгаков', 1),
#     ('Собачье сердце', 'Михаил Булгаков', 1),
#     ('Изучаем Python', 'Марка Лутца', 2),
#     ('Программирование на Python', 'Марка Лутца', 2),
#     ('Python. Карманный справочник', 'Марка Лутца', 2),
#     ('Основы Python. Научитесь думать как программист', 'Аллен Б. Дауни', 2),
#     ('Изучение сложных систем с помощью Python', 'Аллен Б. Дауни', 2),
#     ('Нравственные письма к Луцилию', 'Сенека Луций Анней', 3),
#     ('О краткости жизни', 'Сенека Луций Анней', 3),
#     ('Философские трактаты', 'Сенека Луций Анней', 3),
#     ('Великое учение', 'Конфуций', 3),
#     ('Жемчужины мысли', 'Конфуций', 3),
#     ('Уроки мудрости', 'Конфуций', 3),
#     ('Суждения и беседы', 'Конфуций', 3);

# SELECT * FROM book WHERE book_author = 'Михаил Булгаков';
# SELECT * FROM book WHERE book_title = 'Евгений Онегин';
# SELECT * FROM book WHERE publisher_id = '1';
# SELECT * FROM book WHERE book_author = 'Аллен Б. Дауни';
# SELECT * FROM book WHERE book_title = 'Изучаем Python';
# SELECT * FROM book WHERE publisher_id = '2';
# SELECT * FROM book WHERE book_author = 'Конфуций';
# SELECT * FROM book WHERE book_title = 'Философские трактаты';
# SELECT * FROM book WHERE publisher_id = '3';
