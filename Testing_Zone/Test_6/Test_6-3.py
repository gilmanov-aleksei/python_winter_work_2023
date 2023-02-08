#! /usr/bin/python

import csv

# with open('test.csv', encoding='utf-8') as file:
#     rows = csv.reader(file)
#     for row in rows:
#         print(row)

columns = ['first_name', 'second_name', 'riting']
data = [['1', 'Ivanov', '200'],
        ['2', 'Petrov', '300'],
        ['3', 'Sidorov', '400'],
        ['4', 'Makarov', '500']]

with open('test1.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)

    # data = fi.read()
    # for line in data.splitlines():
    #     print(line.split(','))