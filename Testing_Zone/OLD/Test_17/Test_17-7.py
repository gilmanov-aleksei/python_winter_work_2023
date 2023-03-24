#! /usr/bin/python
#
# class Student:
#     lst = []
#     def __init__(self, name):
#         self.name = name
#         Student.lst.append(self.name)
#
#
# s1 = Student('Emma')
# s1.name
# s2 = Student('Nick')
# print(Student.lst)
# print(isinstance(s1, Student))
# print(s1.__class__)
# print(dir(s1))

class Tree(object):
    def __init__(self, kind, height):
        self.kind = kind
        self.age = 0
        self.height = height

    def grow(self):
        self.age += 1


class FruitTree(Tree):
    col = ''

    def __init__(self, kind='any', height=20):
        super().__init__(kind, height)

    def give_fruits(self):
        print(f'Collected 20 kg of {self.kind}')


f_tree = FruitTree('apple', 0.7)
f_tree.col = 'Red'
print(f_tree.kind, f_tree.age, f_tree.height, f_tree.col)
s_tree = Tree('oak', 1)
s_tree.grow()
print(s_tree.kind, s_tree.age, s_tree.height)
orange = FruitTree('orange', 100)
print(orange.kind, orange.height, orange.age)
f_tree.give_fruits()
orange.give_fruits()
f_tree.grow()
