#! /usr/bin/python

# d = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         d.append(i * i)
#     else:
#         d.append(i ** 3)
# print(d)

# print([i ** 3 if i % 2 else i * i for i in range(1, 11)])

def fun(n):
    yield n, n ** 4
    yield n, n ** 5
    for x in range(n):
        if x % 2 == 0:
            yield x, x * x
            print("--")
        else:
            yield x, x * x * x
            print("---")
        # yield x ** 3 if x % 2 else x ** 2

g = fun(5)

for x, k in g:
    print(f"x = {x} k = {k}")
