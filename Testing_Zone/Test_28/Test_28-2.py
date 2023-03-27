#! /usr/bin/python
#
# def __init__(self, x, y):
#     self.x = x
#     self.y = y
#
#
# Point = type('Point', (), {'__init__': __init__})
#
# p = Point(1, 2)
#
#
# def __str__(self):
#     return str((self.x, self.y))
#
#
# print(p)
# Point.__str__ = __str__
# lst = [(0, 0), (1, 1), (2, 2), (1, 3)]
# point_list = []
# for i in lst:
#     point_list.append(Point(i[0], i[1]))
#
# # for i in point_list:
# #     print(i, type(i))
#
#
# def distance(self, other):
#     import math
#     res = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
#     return math.sqrt(res)
#
#
# Point.distance = distance
# for i in point_list:
#     for j in point_list:
#         if Point.distance(i, j) > 2:
#             print(i, j, Point.distance(i, j))

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# x = Node('x')
# x.next_node = a
# y = x
# while y.next_node != None:
#     y = y.next_node
#     # print(y.value)
# else:
#     y.next_node = x
y = a
z = 1
print(y.value, z)
while y.next_node != None:
    y = y.next_node
    z += 1
    print(y.value, z)
print()

b.next_node = c.next_node
c.next_node = b
a.next_node = c
y = a
z = 1
print(y.value, z)
while y.next_node != None:
    y = y.next_node
    z += 1
    print(y.value, z)