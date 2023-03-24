#! /usr/bin/python

# def func1(m, n):
#     print("func1", n, m)
#     n -= 1
#     m += 1
#     if n > 0:
#         func1(m, n)
#     print("------")
#     print("func2", n, m)
#     return
#
#
# func1(0, 5)

# def fact(n):
#     # if n == 1:
#     #     return 1
#     # else:
#     #     return n*fact(n-1)
#     return 1 if n == 0 else n * fact(n-1)
# print(fact(1))
# print(fact(2))
# print(fact(3))
# print(fact(4))
# print(fact(5))

def triangle(n, m):
    print(' ' * (m - n), '* ' * n)
    if n < m:
        triangle(n + 1, m)
    # print(' ' * (m - n), '* ' * n)
    return


triangle(0, 10)

# def triangle(n, m):
#     print(' *' * n, ' ' * (m - n))
#     if n > m:
#         triangle(n - 1, m)
#     print('* ' * n,' ' * (n-m))
#     return
#
#
# triangle(10, 0)
