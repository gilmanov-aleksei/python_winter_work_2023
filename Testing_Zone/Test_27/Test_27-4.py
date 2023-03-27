#! /usr/bin/python

lst = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (2, 1), (2, 0)]
pname = 'Point'
xyz = type(pname, (), {'x': 0, 'y': 0})
for i in lst:
    s = 'p'+str(i[0])+str(i[1])
    s = xyz()
    s.x = i[0]
    s.y = i[1]


#

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Вектор с координатами ({self.x}, {self.y})"
#
#     def __repr__(self):
#         return f"Vector ({self.x}, {self.y})"

class Point:
    def __init__(self, x, y):
        return

    def __getattr__(name):
        return

    def __setattr__(name):
        return

