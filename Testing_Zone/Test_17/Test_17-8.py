#! /usr/bin/python

class Student:
    def __init__(self, name):
        print("inside constructor")
        self.name = name
        print("object inittalized")
    def show(self):
        print(self.name)

s1 = Student('Emma')