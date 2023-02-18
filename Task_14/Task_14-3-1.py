#! /usr/bin/python

def triangle(m, n=0):
    print(' ' * (m - n), '* ' * n)
    if n < m:
        triangle(m, n + 1)
        print(' ' * (m - n), '* ' * n)
    return


triangle(int(input("Enter num: ")))
