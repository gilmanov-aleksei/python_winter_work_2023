#! /usr/bin/python

import csv

with open('products.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    for row in rows:
        print(row)


    # data = fi.read()
    # for line in data.splitlines():
    #     print(line.split(','))