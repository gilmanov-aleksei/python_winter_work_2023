#! /usr/bin/python

# Задача 19-2
# Реализуйте класс Fibonacci , который реализует итератор,
# генерирующий бесконечную последовательность чисел Фибоначчи.
# Например:
# fibonacci=Fibonacci()
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# Должен печатать следующие числа:
# 1
# 1
# 2
# 3

class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        res = self.curr
        self.curr += self.prev
        self.prev = res
        return res


fibonacci = Fibonacci()
print(next(fibonacci))  # 1
print(next(fibonacci))  # 1
print(next(fibonacci))  # 2
print(next(fibonacci))  # 3

# fibonacci = Fibonacci()
# for i in range(10):
#     print(next(fibonacci), end=' ')
