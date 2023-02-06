#! /usr/bin/python

f = open("text.txt", 'r', encoding='utf-8')
lst = f.readlines()
print(lst)

f.close()