# #! /usr/bin/python
#
# def summ(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summ(n - 1)
#
#
# n = int(input("Enter num: "))
# print(summ(n))

def fib(n):
    if n == 1: return 1
    elif n == 2: return 1
    else:
        return fib(n - 2) + fib(n - 1)


print(fib(int(input("Enter Fibonachi: "))))
