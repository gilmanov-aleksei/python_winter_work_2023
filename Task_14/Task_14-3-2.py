#! /usr/bin/python
def prt_zvezda(m):
    return print(('* ' * m).center(10))


def tri_2_2(n):
    if n > 1:
        prt_zvezda(n)
        tri_2_2(n - 1)
    return prt_zvezda(n)


tri_2_2(5)
