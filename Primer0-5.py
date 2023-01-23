#! /usr/bin/python

n = int(input())
lst = []
for i in range(1, n+1):
    for j in range(i):
        lst.append(j)
print(lst)