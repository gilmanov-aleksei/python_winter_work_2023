#! /usr/bin/python

class Shape:
    def __init__(self, color, per):
        self.color = color
        self.per = per
    def peri(self):
        return self.per
class Triangle(Shape):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def peri(self):
        return self.x + self.y + self.z
