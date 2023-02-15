#! /usr/bin/python

ff = open("test.txt", 'w',  encoding="utf-8")
lst = []
for i in range(9):
    lst.append(f'{i} {i * i} \n')
ff.writelines(lst)

ff.close()