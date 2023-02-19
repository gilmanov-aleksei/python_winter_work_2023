#! /usr/bin/python


def tri_2_1(n):
    if n > 1:
        print(('* ' * n).center(10))
        tri_2_1(n - 1)
    print(('* ' * n).center(10))
    return


tri_2_1(5)

# n = 5
# for i in range(n * 2 - 1, 0, -2):
#     print(('*' * i).center(n * 2))
# for i in range(1, n * 2, 2):
#     print(('*' * i).center(n * 2))


# def spruce(n, i=1):
#     if i <= n * 2:
#         print(("*" * i).center(n * 2, " "))
#         spruce(n, i + 2)
#
# spruce(5)

# def f(n, level=0):
#     if n > 1:
#         f(n-1, level+1)
#         for j in range(n):
#             print(' '*(n-j+level)+'*'*(2*j+1))
# f(5)

# def f(n, level = 1):
#     if n > 0:
#         print(' '*(n-1)+'*'*(level*2-1))
#         f(n-1, level+1)
# f(5)

# def f(n, level = 1):
#     if n > 1:
#         print(' '*(n-1)+'*'*(level*2-1))
#         f(n-1, level+1)
#     elif n == 1:
#         print(' '*(level-1)+'*')
# f(7)
