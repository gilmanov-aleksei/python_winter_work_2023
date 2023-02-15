#! /usr/bin/python

lst = [1, 10, 100, 2, 20, 200]


# [1, 10, 100, 2, 20, 200]
# 1, 11, 111, 113, 133, 333
def su():
    t = 0
    for v in lst:
        t += v
        yield t


gf = su()
for x in gf:
    print(x)
