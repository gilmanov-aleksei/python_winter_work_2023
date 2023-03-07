#! /usr/bin/python

# Задача 20-3
# Создайте класс, экземпляр которого генерирует бесконечную
# циклическую последовательность из чисел и больших латинский букв.
# 1,A,2,B,3,C, ..,X,25,Y,26,Z,1,A,2,B,3,C, X,25,Y,26,Z

# class InfiniteSequence:
#     def __init__(self):
#         self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                          'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#         self.index = 0
#
#     def next(self):
#         if self.index % 2 == 0:
#             value = self.index // 2 + 1
#         else:
#             value = self.alphabet[self.index // 2]
#
#         self.index += 1
#         if self.index == 52:
#             self.index = 0
#
#         return value
# infseq = InfiniteSequence()
# for i in range(5):
#     print(next(infseq.next()))

class InfiniteSequence:
    def __init__(self):
        self.counter = 0
        self.letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

    def generate_sequence(self):
        while True:
            if self.counter % 2 == 0:
                yield str(self.counter // 2 + 1)
            else:
                yield self.letters[self.counter // 2]
            self.counter = (self.counter + 1) % 52


sequence = InfiniteSequence()
for i in range(10):
    print(next(sequence.generate_sequence()))
