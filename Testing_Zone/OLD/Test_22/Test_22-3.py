#! /usr/bin/python

import psycopg2
import pandas as ps

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="12345678",
    host="127.0.0.1",
    port="5432"
)
cur = con.cursor()
cur.execute("INSERT INTO pupil VALUES (2, 'Вася', 1)")
cur.execute('SELECT * FROM pupil')
d = {'id': [], 'name': [], 'result': []}
for i in cur.fetchall():
    print(i)
    d['id'].append(i[0])
    d['name'].append(i[1])
    d['result'].append(i[2])
# con.commit()
con.close()
