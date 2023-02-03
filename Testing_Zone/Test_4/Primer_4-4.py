#! /usr/bin/python

#lst = [22, 11, 13, 14, 36, 1, 2]
#print(sorted(lst, key = lambda x:(x % 2, x)))

# lst = ['b', 'A', 'Z', 'x']
# print(sorted(lst, key = lambda x: x.lower()))

lst = [1, 10, 21, 30]
x = 16
print(min(lst, key=lambda y: abs(x - y)))

lst = [123, 234, 345, 456]
sum_dig = lambda x: sum(map(int, str(x)))
print(list(map(sum_dig, lst)))
