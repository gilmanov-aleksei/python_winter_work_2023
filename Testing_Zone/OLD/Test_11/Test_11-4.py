#! /usr/bin/python

import re
# text = "Java самый популятрный язык программирования в 2023 году."
# res = re.sub(r'Java', r'Python', text)
# print(res)
#
# text2 = " abc def xyzu 12"
# res2 = re.sub(r'\b\w{3}\b', r'===', text2)
# print(res2)
#
# text3 = "Java самый популятрный язык программирования в 2023 году."
# res3, n = re.subn(r'Java', r'Python', text3)
# print(res3,"-", n)

# text = "http://www.dhfhdfjhg.ru http://www.fdhuidhj.ru"
# res = re.sub(r'http://www\.\w+\.ru', r'http://www.rbc.ru', text)
# print(text)
# print(res)

text = "(095)5340951 (095)3467823 (095)0953478"
res = re.sub(r'\(095\)', r'(812)', text)
print(text)
print(res)