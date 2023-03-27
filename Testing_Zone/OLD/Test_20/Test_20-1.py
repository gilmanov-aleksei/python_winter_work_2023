#! /usr/bin/python

# a = {True: '1', 1: 'one'}
# print(a)
# a = {1: '1', True: 'one'}
# print(a)
# a = {False: '0', 0: 'zero'}
# print(a)
# a = {0: '0', False: 'zero'}
# print(a)

import itertools

# for j in range(1, 4, 1):
#     for x in itertools.combinations([1, 2, 3, 4], j):
#         print(x, end='')

print(list(zip([1,2,3], [11,22,33,44])))

print(list(itertools.zip_longest([1,2,3], [11,22,33,44], [111, 222, 333, 444, 555])))
