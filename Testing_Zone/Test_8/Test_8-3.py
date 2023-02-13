#! /usr/bin/python


print([x ** 2 for x in range(0, 50) if x % 10 == 0])

#! /usr/bin/python

a = [x for x in range(21) if x %2 == 1]
print(a)
a = [x for x in range(21) if x %2 == 0]
print(a)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)