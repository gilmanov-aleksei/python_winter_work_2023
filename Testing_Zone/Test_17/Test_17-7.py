#! /usr/bin/python

class Student:
    lst = []
    def __init__(self, name):
        self.name = name
        Student.lst.append(self.name)


s1 = Student('Emma')
s1.name
s2 = Student('Nick')
print(Student.lst)
print(isinstance(s1, Student))
print(s1.__class__)
print(dir(s1))