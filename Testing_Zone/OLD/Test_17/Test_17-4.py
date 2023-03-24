#! /usr/bin/python

class Pet:
    def __init__(self, name, massa, hungry_level):
        self.name = name
        self.massa = massa
        self.hungry_level = hungry_level

    def info(self):
        print(f'Питомца зовут: {self.name}. Его вес: {self.massa} грамм, он сыт на {self.hungry_level}')

    def hungry(self):
        if self.hungry_level <= 5: return 'голоден'
        elif self.hungry_level >= 10: return 'сыт'

    def feed(self, h):
        self.hungry_level += h


a = Pet('Boy', 2500, 3)
b = Pet('Kiss', 3000, 5)
c = Pet('Joy', 7000, 7)

a.info()
b.info()
c.info()
