#! /usr/bin/python

class Sinleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sinleton, cls).__new__(cls)
        return cls.instance


s1 = Sinleton()
s2 = Sinleton()
print(s1 is s2)
s1.x = 123
print(s2.x)
