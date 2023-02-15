#! /usr/bin/python

n = int(input())
def factorial():
    f, k = 1, 1
    while True:
        yield k, f
        k += 1
        f += k # f *= k


gf = factorial()
for _ in range(n):
    print(next(gf))
