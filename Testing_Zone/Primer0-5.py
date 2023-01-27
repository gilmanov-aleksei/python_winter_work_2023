#! /usr/bin/python

# primer = input('Введите пример: ').split()
primer = '1 + 2'
p = primer.split()
print(p)
dict_p = {}
print(dict_p)
    # Подсчитываем каждый символ w1 в словаре.
for i in range(1, len(p) + 1):
    dict_p[i] = 0
#   dict_p.get(w1[i], 0) + 1

print(dict_p)
print(p[0], p[1], p[2], '=', int(p[0])+int(p[2]))
