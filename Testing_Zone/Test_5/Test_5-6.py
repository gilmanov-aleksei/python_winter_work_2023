#! /usr/bin/python

fr = open("test.txt", 'r', encoding="utf-8")
fw = open("test1.txt", 'w', encoding="utf-8")

lst = fr.readlines()

for i in lst:
    if any(x.isdigit() for x in i):
        fw.writelines(i)

fw.close()
fr.close()

