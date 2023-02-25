#! /usr/bin/python

# import re
#
# text = 'http://www.lksjflskj.ru'
# res, n = re.subn(r'Java', r'Python', text)
# print(res, n)

import re

text = 'fizz.123.buzz.456.fizzbuzz'
res1 = re.sub(r'\d+', r'#', text)
res2 = re.sub(r'[a z]+', r'(*)', text)
print(res1)
print(res2)
