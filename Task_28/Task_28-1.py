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


print("Компактый код, который выполняется за время O(n^2)")
a = [1, 2, 3, 4, 5]
print(find_inversions_num(a), "[1,2,3,4,5] -> 0")
a = [5, 4, 3, 2, 1]
print(find_inversions_num(a), "[5,4,3,2,1] -> 10")


def merge_sort(arr, inv_count=0):
    if len(arr) <= 1:
        return arr, inv_count
    mid = len(arr) // 2
    left, inv_count = merge_sort(arr[:mid], inv_count)
    right, inv_count = merge_sort(arr[mid:], inv_count)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inv_count


def find_inversion_num(lst):
    _, inv_count = merge_sort(lst)
    return inv_count


print("Быстрый код, который выполняется за время O(n * log(n))")
a = [1, 2, 3, 4, 5]
print(find_inversion_num(a), "[1,2,3,4,5] -> 0")
a = [5, 4, 3, 2, 1]
print(find_inversion_num(a), "[5,4,3,2,1] -> 10")
