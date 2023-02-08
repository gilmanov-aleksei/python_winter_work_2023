#! /usr/bin/python

with open('test.csv') as fi:
    data = fi.read()
    for line in data.splitlines():
        print(line.split(','))
