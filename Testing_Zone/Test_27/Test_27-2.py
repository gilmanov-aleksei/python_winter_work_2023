#! /usr/bin/python

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Вектор с координатами ({self.x}, {self.y})"
#
#     def __repr__(self):
#         return f"Vector ({self.x}, {self.y})"
#
#
# v = Vector(2, 3)
# print(str(v))
# print(repr(v))
# print(v)


# class Anyclass:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             self.__setattr__(k, v)
#
#     def __str__(self):
#         res = 'Anyclass:'
#         for k, v in self.__dict__.items():
#             res += ' ' + str(k) + ':' + str(v) + ','
#         return res.strip(',')
#
#     def __repr__(self):
#         res = 'Anyclass('
#         for k, v in self.__dict__.items():
#             res += str(k) + '=' + str(v) + ','
#         return res.strip(',') + ')'
#
#
# a1 = Anyclass(a=1, b=123, x=77)
# a2 = Anyclass()
# a3 = Anyclass(k='dhfdjhjk')
# a3.k = 'xyz'
# print(str(a1))
# print(str(a2))
# print(str(a3))
#
# print(repr(a1))
# print(repr(a2))
# print(repr(a3))


# xyz = type('ClassA', (), {})
# x = xyz()
# print(type(x))
#
# strb = input()
# zyx = type(strb, (), {})
# b = zyx()
# print(type(b))
