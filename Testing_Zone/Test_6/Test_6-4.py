#! /usr/bin/python

lst = []
with open('test.txt', 'r', encoding='utf-8') as fi:
    for i in fi:
        lst.append(i.strip())
    print(lst)
