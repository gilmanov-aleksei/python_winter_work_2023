# #! /usr/bin/python
#
# def fu(x):
#     return 'FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x
#
#
# a = [fu(x) for x in range(20)]
# print(a)
#
# words = ['Я', 'изучаю', 'Python']
# res = [letter for word in words for letter in word]
# print(res)
#
# matrix = [[i ** j for i in range(5)] for j in range(6)]
# print(matrix)
#
# matrix = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2],
# ]
# flat = [num for row in matrix for num in row]
# print(flat)
#
# t = [[x * y for x in range(1, 6)] for y in range(1, 6)]
# print(t)
#
# d = {}
# for num in range(1, 10):
#     d[num] = num ** 2
# print(d)

# d={num: num **2 for num in range(1.10)}
# rus_let = 'воититивоиытл12543265@#@%$^%&^'
# dct = {i:ord(i) for i in rus_let}
# print(dct)

# items = [('c', 3), ('d', 4), ('a', 1), ('b', 2)]
# disc_variable = {key: value for (key, value) in items}

# names = ['Fizz', 'Buzz', 'FizzBuzz']
# inedx = {k: v for (k, v) in enumerate(names)}
# print(inedx)
# def fb(x):
#     return 'FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x
#
#
# d = {i: fb(i) for i in range(10) if type(fb(i)) != str}
# print(d)
