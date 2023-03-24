#! /usr/bin/python

import time


# def two_sleep():
#     t0 = time.time()
#     time.sleep(2)
#     t1 = time.time()
#     return t1 - t0


# def three_sleep(s):
def sleeping(s):
    t0 = time.time()
    time.sleep(s)
    t1 = time.time()
    return t1 - t0

two = 0
three = 0

for i in range(11):
    if i % 2 == 0:
        # print(i, '- two')
        two += sleeping(2)
    else:
        # print(i, '- three')
        three += sleeping(3)
print('two sleep: ', two)
print('three sleep: ', three)
