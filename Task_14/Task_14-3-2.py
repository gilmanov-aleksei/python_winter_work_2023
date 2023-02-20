#! /usr/bin/python
def prt_zv(m):
    return print(('* ' * m).center(10))


def tri_2_2(n):
    if n > 1:
        prt_zv(n)
        tri_2_2(n - 1)
    return prt_zv(n)


def tri_2_3(n):
    if n > 1: prt_zv(n) or tri_2_3(n - 1) or prt_zv(n)
    return


tri_2_2(5)
input("Press Enter")
tri_2_3(5)
