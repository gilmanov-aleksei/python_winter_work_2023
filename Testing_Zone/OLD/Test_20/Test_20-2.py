#! /usr/bin/python

import numpy as np
#
# arr = np.array([5, 3, 2, 0, 7, 12, 9, 1, 3, 4])

# lst1 = [4, 5, 6, 7]
# lst2 = [7, 8, 9, 10]
# arr1 = np.array(lst1)
# arr2 = np.array(lst2)
# print(arr1, arr2)
# print(arr1 / arr2)

# lst1 = np.zeros((2,3), dtype='int')
# lst2 = np.ones((2,3), dtype='int')
# a = lst1.reshape(6)
# print(lst1)
# print(lst2)
# print(a)

# import numpy as np
#
# lst = np.array([[1, 2, 4], [10, 20, 30], [100, 200, 300]])
# print(np.sum(lst))
# print(np.sum(lst, axis=0)) # сложение по столбцам
# print(np.sum(lst, axis=1)) # сложение по строкам
# print(np.sqrt(lst))
# print(np.cbrt(lst))
# print(np.abs(lst))
# print(np.exp(lst))
# print(np.gcd(lst, 2))
# print(np.lcm(lst, 1))

# import numpy as np
#
# x = np.array([[1, 2, 3, 4, 5, np.nan], [10, 20, 30, 40, 50, 60]])
# print(np.mean(x, axis=0))
# print(np.mean(x, axis=1))
# print(np.average(x, weights=None))
# print(np.amax(x))
# print(np.amix(x))

# import numpy as np
#
# x = np.array([1, 5, 2, 15, 3])
# y = np.array([2, 5, 6, 8, 10])
# condition = x > 4
# print(x[condition])

# import numpy as np
#
# arr = np.array([2, 7, 7, 8, 8, 6, 8, 7, 6, 7])
# condition = arr < np.percentile(arr, 25)
# print(arr[condition])


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
#
# import numpy as np
#
# n = int(input("Enter n: "))
# # n = 3
# lst = list(range(1, n * n + 1))
# # a = np.arange(n * n).reshape(4, 3)
# x = np.array(lst)
# y = x.reshape((n, n))
# print(y)
# print(np.median(y))
# print(np.median(y, axis=0))
# print(np.median(y, axis=1))
#
