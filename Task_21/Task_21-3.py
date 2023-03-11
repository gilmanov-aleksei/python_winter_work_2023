#! /usr/bin/python


# Для создания таблицы "book" с указанными полями в PostgreSQL,
# необходимо выполнить следующий SQL-запрос:

# CREATE TABLE book (
#   book_id serial PRIMARY KEY,
#   book_title text,
#   book_author text,
#   publisher_id integer
# );

# Для вставки нескольких книг, выполните SQL-запрос типа INSERT:
#
# INSERT INTO book (book_title, book_author, publisher_id) VALUES
#     ('1984', 'Джордж Оруэлл', 1),
#     ('Мастер и Маргарита', 'Михаил Булгаков', 2),
#     ('Преступление и наказание', 'Федор Достоевский', 3);
# Здесь мы добавляем три книги разных авторов в таблицу "book".
# Чтобы выбрать все книги автора "Джордж Оруэлл", выполните SQL-запрос типа SELECT:
# SELECT * FROM book WHERE book_author = 'Джордж Оруэлл';
# Аналогично, чтобы выбрать книги с определенным названием, выполните запрос типа SELECT:
# SELECT * FROM book WHERE book_title = 'Преступление и наказание';
