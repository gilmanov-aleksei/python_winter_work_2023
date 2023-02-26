#! /usr/bin/python

# import re
#
# text = 'http://www.lksjflskj.ru'
# res, n = re.subn(r'Java', r'Python', text)
# print(res, n)

import re

text = 'fizz.123.buzz.456.fizzbuzz'
res1 = re.sub(r'\d+', r'#', text)
res2 = re.sub(r'[a-z]+', r'(*)', text)
print(res1)
print(res2)

# import re

# def fullname(x):
#     # x специальный объект, который содержит значение, индекс начала
#     # и конца
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     match s:
#         case 'Коля':
#             return 'Николай'  # Коля 12 16
#         case 'Миша':
#             return ' Михаил'  # Миша 26 30
#
#
# # if s == 'Коля': return 'Николай'
# # elif s == 'Миша': return 'Михаил'
#
# text = 'Здравствуй, Коля! Привет, Миша!'
# print(re.sub(r"\b\w{4}\b", fullname, text))

# import re


# def aeroport(x):
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     match s:
#         case 'LED':
#             return 'Пулково'
#         case 'MSQ':
#             return 'Минск'
#         case 'SVO':
#             return 'Шереметьево'
#         case 'SVX':
#             return 'Кольцово'
#
#
# text = 'Я вылетаю из LED и лечу через SVO, могу лететь в MSQ через SVX'
#
# print(re.sub(r"\b\w{3}\b", aeroport, text))
