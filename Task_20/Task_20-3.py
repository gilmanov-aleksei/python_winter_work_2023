#! /usr/bin/python

# Задача 20-3
# Создайте класс, экземпляр которого генерирует бесконечную
# циклическую последовательность из чисел и больших латинский букв.
# 1,A,2,B,3,C,...,X,25,Y,26,Z,1,A,2,B,3,C,X,25,Y,26,Z

class InfSeq:  # Создаём класс бесконечный цикл
    def __init__(self):  # Инициализация
        self.index = 0  # Устанавливаем индекс на 0
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Алфавит

    def __iter__(self):  # Итератор
        return self

    def __next__(self):
        self.index += 1  # Увеличиваем индекс на 1
        if self.index >= 53:  # Если индекс вышел за пределы (26 х 2),
            self.index = 1  # то сбрасываем индекс на 1
            return 'A'  # и возвращаем букву А
        if self.index % 2 == 0:  # проверка на чётность
            return self.index // 2  # если четное, печатаем цифру
        else:
            return self.alphabet[self.index // 2]  # если нечетное, то букву


iseq = InfSeq()

for i in range(57):
    print(next(iseq), end=',')
