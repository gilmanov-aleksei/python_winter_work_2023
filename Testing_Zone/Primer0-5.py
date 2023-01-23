#! /usr/bin/python

crl = (123, 234, 345, 456, 567, 678, 789, 890)
n = int(input())
for k,v in enumerate(crt):
    if n => v and n <= crt[k+1]:
        res = crt[:k+1]+(n,)+crt[k+1:]
        break
print(res)
