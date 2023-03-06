#! /usr/bin/python

# import numpy as np
#
# x = np.array([3, 5, 1, 8, 14, 17, 3, 10, 15, 18])
# y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# z = np.where(x > 5, x, y)
# print(z)

# import numpy as np
#
# x = np.array([3, 5, 1, 8, 14, 17, 3, 10, 15, 18])
# z = np.sort(x)
# print(z)

# import numpy as np
#
# x = np.array([[1,2,3,4], [5,6,7,8]])
# stroki, stold = x.shape
# print(stroki)
# print(stold)

import numpy as np

n = int(input("Enter n: "))
# n = 3
lst = list(range(1, n * n + 1))
# a = np.arange(n * n).reshape(4, 3)
x = np.array(lst)
y = x.reshape((n, n))
print(y)
print(np.median(y))
print(np.median(y, axis=0))
print(np.median(y, axis=1))

