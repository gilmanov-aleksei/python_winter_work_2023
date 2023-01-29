#! /usr/bin/python

n = int(input("Номер элемента ряда Фибоначчи: "))
f1 = 1
f2 = 1
fs = 0
i = 0
while i < n - 2:
    fs = f1 + f2
    f1 = f2
    f2 = fs
    i += 1

print("Значение этого элемента:", f2)

fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
