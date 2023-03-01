#! /usr/bin/python

class Shape:
    def __init__(self, per, col):
        self.per = per
        self.col = col
    def peri(self):
        return self.per
    def __str__(self):
        return self.col + str(self.per)

s = Shape(10, 'Red')
print(s.per, s.col)
z = Shape(20, 'Blue')
print(z)

