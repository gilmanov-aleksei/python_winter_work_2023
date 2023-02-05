#! /usr/bin/python

# Дан список слов. Отсортируйте его по количеству уникальных букв
# в каждом слове в обратном порядке.
# Например:  ['abab', 'xx', 'aaaaaaa', 'abcbab']
# Результат:  ['abcbab', 'abab', 'aaaaaaa', 'xx']
# Если число уникальных букв одинаково, то порядок алфавитный.

lst = ['abab', 'xx', 'aaaaaaa', 'abcbab']
elm = {}
print(lst)
for i in lst:
    elm[i] = len(set(i))
print(elm)
sort_t = sorted(elm.items(), key=lambda x: x[1], reverse=True)
print(dict(sort_t))

