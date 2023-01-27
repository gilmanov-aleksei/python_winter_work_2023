#! /usr/bin/python

n = int(input())
sinon = {}

for i in range(n):
    s,z = input().split()
    sinon[s] = z
    sinon[z] = s
print(sinon)
while True:
    x = input()
    print(sinon.get(x, "нет синонима"))
    if x == "stop":
        break

