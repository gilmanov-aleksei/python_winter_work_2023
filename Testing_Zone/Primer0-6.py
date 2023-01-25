#! /usr/bin/python

abc = {}
s = input()
for i in s:
    if i not in abc:
        abc[i] = 0
    abc[i] += 1
print(abc)
