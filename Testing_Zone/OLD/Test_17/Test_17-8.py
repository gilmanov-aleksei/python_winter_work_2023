#! /usr/bin/python
#
# class Shape:
#     def __init__(self, col = 'Red', per = 0):
#         self.col = col
#         self.per = per
#     def peri(self):
#         return self.per
# class Triangle(Shape):
#     def __init__(self, x, y, z):
#         super().__init__()
#         self.x = x
#         self.y = y
#         self.z = z
#     def peri(self):
#         return self.x + self.y + self.z
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__()
#         self.a = a
#         self.b = b
#     def peri(self):
#         return 2 * (self.a + self.b)
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#
# s = Square(7)
# print(s.peri())


# s = Shape('Blue', 5)
# print(s.col, s.peri())
# t = Triangle(3, 4, 5)
# print(t.peri(), t.col)
# r = Rectangle(10, 20)
# print(r.peri(), r.col)
#
# class Horse:
#     isHorse = True
#     def Igogo(self): return 'Igogo'
# class Donkey:
#     isDonkey = True
#     def Iaia(self): return 'Iaia'
# class Mule(Horse, Donkey):
#     pass
# mu = Mule
# print(mu.isHorse)
# print(mu.isDonkey)

#
# class Triangle():
#     def tr_check(x, y, z):
#         if x > 0 and y > 0 and z > 0:
#             if x + y > z and y + z > x and z + x > y:
#                 return True
#         return False
#
#     def __init__(self, x, y, z):
#
#         if Triangle.tr_check(x, y, z):
#             self.x = x
#             self.y = y
#             self.z = z
#         else:
#             print('NO!!!')
#
#
# t = Triangle(3, 4, 5)
# print(t.)