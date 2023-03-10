#! /usr/bin/python

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cur_money = self.money

    def info(self):
        print(f'Меня зовут {self.name}. У меня {self.cur_money} рублей')

    def set_money(self, x):
        self.money += x

    def get_money(self):
        return self.cur_money

    def give_money(self, other, x):
        if self.cur_money >= x:
            other.money += x
            self.cur_money -= x
        else:
            print(f'У {self.name} не хватает {x - self.cur_money} рублей')


a = Person('Pete', 200)
b = Person('Nick', 300)
c = Person('Jack', 500)

a.info(), b.info(), c.info()
c.give_money(a, 200)
c.give_money(b, 200)
a.info(), b.info(), c.info()
c.give_money(b, 200)
a.info(), b.info(), c.info()
