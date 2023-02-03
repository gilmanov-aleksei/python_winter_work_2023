#! /usr/bin/python

import math

data = list(map(int, input("Enter numbers: ").split()))
print("НОД =", math.gcd(*data))
print("НОК =", math.lcm(*data))
