#! /usr/bin/python
#
# class Shape:
#     def __init__(self, per, col):
#         self.per = per
#         self.col = col
#     def peri(self):
#         return self.per
#     def __str__(self):
#         return self.col + str(self.per)
#
# s = Shape(10, 'Red')
# print(s.per, s.col)
# z = Shape(20, 'Blue')
# print(z)
#


class Student:
    def __init__(self, name):
        print('inside constructor')
        self.name = name
        print('object inittalized ' + self.name)

    def show(self):
        print(self.name)

    def __del__(self):
        print('inside destructor')
        print('object destroyed')


s1 = Student('Emma')
s2 = Student('Nick')
input()
del s2
input()
s1.show()
s2.show()
