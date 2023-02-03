#! /usr/bin/python

import math

data = list(map(int, input("Enter numbers: ").split()))
gcd = math.gcd(*data)
lcm = math.lcm(*data)
print("НОД =", gcd)
print("НОК =", lcm)
