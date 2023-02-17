#! /usr/bin/python

# def fun_gen(n):
#     for x in range(n):
#         yield x
#
# g = fun_gen(5)
# print(*g)

# def fun_gen(n):
#     yield from range(n)
#
# g= fun_gen(5)
# print(*g)

# def fun_gen1():
#     yield from "Red"
#     yield from "Green"
#     yield from "Blue"
#
# def fun_gen2():
#     yield from "Krug"
#     yield from "Kvadrat"
#     yield from fun_gen1()
#
# print(*fun_gen2())

# list_comp = [x for x in range(10)]
# print(list_comp)
# gen_expr=(x for x in range(10))
# for x in gen_expr:
#     print(x, end=" ")

# def integers(n):
#     for i in range(1, n + 1):
#         yield i
#
#
# def evens(iterable):
#     for i in iterable:
#         if not i % 2:
#             yield i
#
#
# def squared(iterable):
#     for k in iterable:
#         yield k * k
#

# chain = squared(evens(integers(10)))
# chain = [x for x in squared(evens(integers(10)))]
# print(chain)
#
# def gen1(n):
#     x = ord('а')
#     z = ord('я')
#     yield from range(x, x + n)
#
#
# def gen2(x):
#     for i in x:
#         yield chr(i).upper()
#
#
# chain = [x for x in gen2(gen1(33))]
# print(*chain)
