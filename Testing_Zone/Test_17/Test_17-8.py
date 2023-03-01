#! /usr/bin/python

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
