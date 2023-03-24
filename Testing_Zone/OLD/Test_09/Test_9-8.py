#! /usr/bin/python


def su():
    x = 0
    while True:
        x += 1
        for _ in range(x):
            yield x


gf = su()
for x in gf:
    print(x, end=" ")
