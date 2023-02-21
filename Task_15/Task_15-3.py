#! /usr/bin/python

# Задача 15-3
# Напишите функцию, которая находит в строке все телефонные номер,
# которые удовлетворяют следущим цаблонамЖ
# +7(812)DDD-DDDD, +7(812)DDD-DD-DD, +7(921)DDD-DDDD, +7(921)DDD-DD-DD
# где D любая цифра

import re

str = "+7(095)118-1920 +7(822)118-12-78 jdhkdhfkjd +7(495)183-65-65 " \
      "+7(812)183-6999, 812-78-78 +7(927)470-1357, +7(921)499-7531, " \
      "+7(927)670-3355, skjdkljlj +7(9241)679-24-68, +7(923)810-2002, " \
      "+7(812)183-69-45, +7(925)470-4567, +7(ABD)DCF-AB-BD +7(921)499-33-77, " \
      "+7(927)670-1736, ылвладодлов, +7(921)6794455, +7(937)810-0360"

print(*re.findall(r'\+7\(812\)\d{3}-\d{2}.?\d{2}\b|\+7\(921\)\d{3}-\d{2}.?\d{2}\b', str))
