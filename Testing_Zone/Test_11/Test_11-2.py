#! /usr/bin/python

st = "Числа 99, 272, 81 и 999 деляться на на 9"
import re
print(re.findall(r" \d{2},", st))