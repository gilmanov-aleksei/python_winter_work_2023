#! /usr/bin/python



# WHERE supply.title NOT IN
# (SELECT title FROM book)
# (2, 'Достоевский Ф.М.'),
# (3, 'Есенин С.А.'),
# (4, 'Пастернак Б.Л.');

# (book_id int Primary key,
# title varchar(50),
# price int,
# amount int,
# autor_id integer)
# SELECT * FROM supply
# INSERT INTO supply VALUES
# (1, 'Война и мир', 1000, 5, 5),
# (2, 'Стихотворения', 300, 2, 4),
# (3, 'Архепела гулал', 500, 7, 3),
# (4, 'Белая гвардия', 600, 2, 5),
# (5, 'День Опричника', 540, 1, 9);
# INSERT INTO book (book_id, title, author, price, amount)
# SELECT book_id + 7, title, author, price, amount FROM book;


#
# ALTER TABLE book ADD COLUMN author_id int;
# UPDATE book SET author_id = 1 WHERE author LIKE 'Б%'
# UPDATE book SET author_id = 2 WHERE author LIKE 'Д%'
# UPDATE book SET author_id = 3 WHERE author LIKE 'Е%'
# ALTER TABLE book DROP author