#! /usr/bin/python


n = int(input("Номер элемента ряда Фибоначчи: "))
f1 = 1
f2 = 1
fs = 0
i = 0
while i < n - 2:
    fib_sum = f1 + f2
    fib1 = fib2
    fib2 = fib_sum
    i += 1

print("Значение этого элемента:", fib2)