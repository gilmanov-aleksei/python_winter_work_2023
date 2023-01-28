#! /usr/bin/python

print("Треугольник Паскаля")
n = int(input("Введите число: "))
lst = []
while n != 0:
    lst = [1] + lst
    for i in range(1, len(lst) - 1):
        lst[i] += lst[i + 1]
    print(f"{' ' * n}{str(lst)}")
    n -= 1

