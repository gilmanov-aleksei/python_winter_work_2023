#! /usr/bin/python
#
# def fun(n):
#     for x in range(n):
#         yield x * x
# g = fun(3)
# for k in g:
#     print(k)
#     print(type(g))
def fun(n):
    for x in range(n):
        print("До yield", x)
        yield x * x
        print("После yield")
        print(x ** 3)
g = fun(5)

for k in g:
    print("Перед печатью x * x")
    print(f"k = {k}")
    print("После печати x * x")