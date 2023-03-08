#! /usr/bin/python

# Задача 20-3
# Создайте класс, экземпляр которого генерирует бесконечную
# циклическую последовательность из чисел и больших латинский букв.
# 1,A,2,B,3,C,...,X,25,Y,26,Z,1,A,2,B,3,C,X,25,Y,26,Z

class InfSequence:
    def __init__(self):
        self.index = 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == 54:
            self.index = 1
            return 'A'
        elif self.index > 52:
            self.index = 1
        if self.index % 2 == 0:
            return self.index // 2
        else:
            return self.alphabet[self.index // 2]


seq = InfSequence()

for i in range(57):
    print(next(seq), end=',')
