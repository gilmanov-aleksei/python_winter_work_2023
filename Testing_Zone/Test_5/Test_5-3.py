#! /usr/bin/python

ff = open("test.txt", encoding="utf-8")

for i, line in enumerate(ff, 1):
    print(i, line.rstrip())
ff.close()