#! /usr/bin/python

spi = [222, 21, 1, 111, 12, 322]

print(sorted(spi, key=lambda x: x % 10))
print(sorted(spi, key=lambda x: (x % 10, x)))