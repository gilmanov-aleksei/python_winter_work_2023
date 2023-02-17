#! /usr/bin/python

def triangle(n, m):
    print(' ' * (m - n), '* ' * n)
    if n < m:
        triangle(n + 1, m)
    # print(' ' * (m - n), '* ' * n)
    return


triangle(0, 5)
