#! /usr/bin/python

# class X(str):
#     def __init__(self, s):
#         self.s = s
#     def __add__(self, other):
#         return other.s + self.s
# class Y()

# class SomeClass():
#     def __init__(self):
#         self.__param = 42
#
# obj = SomeClass()
# # obj.__param
# obj._SomeClass__param

class Date:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)


lesson = Date('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marivanna = Teacher()
vasy = Pupil()
pety = Pupil()

marivanna.teach(lesson[2], vasy, pety)
marivanna.teach(lesson[0], pety)

print('Vasy', vasy.knowledge)
print('Pety', pety.knowledge)
