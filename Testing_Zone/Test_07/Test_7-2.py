#! /usr/bin/python

import time

t0 = time.time()
# t = (2023, 2, 10, 19, 58, 0, 4 ,0 ,0)
# print(time.asctime(t))
print(time.ctime(t0))
time.sleep(6)
t1 = time.time()
print(time.ctime(t1))
print(f'Длительность: {round(t1 - t0)} сек.')

# x = 1000000
# for i in range(0, x * 10, x):
#     t0 = time.time()
#     su = 0
#     for j in range(i):
#         su += 1
#     t1 = time.time()
#     print(i, t1 - t0)


