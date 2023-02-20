#! /usr/bin/python

import sys
print(sys.version)
print(sys.getrecursionlimit())

a = print(10)
print(a or "a")
print(a, "a")


#! /usr/bin/python

res = []


def list_proc(lst):
    print(lst)

    for x in lst:
        if type(x) == list:
            list_proc(x)
        else:
            res.append(x)
    print(res)
    return res


lst = [1, 2, [11, 22, [111, 222, [1111, 2222, 33333], 333, 444, [555, 666]], 3], 4]

print(list_proc(lst))
