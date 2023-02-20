#! /usr/bin/python
def prt_zvezda(m):
    return print(('* ' * m).center(10))

def tri_2_2(n):
    if n > 1:
        prt_zvezda(n)
        tri_2_2(n - 1)
    return prt_zvezda(n)

def tri_2_3(n):
    if n > 0:
        prt_zvezda(n) or tri_2_3(n - 1) or prt_zvezda(n)
    return


tri_2_2(5)
input("Press Enter")
tri_2_3(5)
