#! /usr/bin/python

f = open("test.txt", encoding="utf-8")
# print(f.read())
lst = f.readlines()
print(lst)

for i, j in enumerate(lst, 1):
    print(i, '-', j.rstrip())


f.close()