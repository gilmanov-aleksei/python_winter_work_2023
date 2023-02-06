#! /usr/bin/python

f = open("test.txt", encoding="utf-8")
# print(f.read())
print(f.readlines())

f.close()