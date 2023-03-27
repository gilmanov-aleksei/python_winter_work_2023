#! /usr/bin/python

# Задача 28-1

# Дан список числе a. Назавем пару (a[i], a[j] инверсией, если i < j,
# а a[i] > a[j]. Напишите функцию, которая возвращает количество инферсий в списке.
# Например:
# [1,2,3,4,5] -> 0
# [5,4,3,2,1] -> 10


def find_inversions_num(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i < j:
                if lst[i] > lst[j]:
                    count += 1
    return count

a = [1, 2, 3, 4, 5]
print(find_inversions_num(a), "[1,2,3,4,5] -> 0")
a = [5, 4, 3, 2, 1]
print(find_inversions_num(a), "[5,4,3,2,1] -> 10")
