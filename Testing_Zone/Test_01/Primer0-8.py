#! /usr/bin/python

lst = list(map(int, input().split()))
abc = {}
for k,v in enumerate(lst):
    if v not in abc:
        abc[v] = []
    abc[v].append(k)
print(abc)



