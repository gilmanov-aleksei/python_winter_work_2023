#! /usr/bin/python

# Задача 15-2
# Напишите функцию, которая принимаетстроку символов,
# и печатет все содержащиеся в ней номера автомашин по
# следующиму правилу: LDDDLL78 или LDDDLL178,
# где L- буквы, сопадающие начертанию в русском и латинском
# алфавите, D - цифра от 0 до 9.
# Например, А123ВС78 или Х666Х178


# lat = "ABCEHKMOPTYX"
# rus = "АВЕКМНОРСТУХ"

import re

str = "L753LL78, L183LL178, L118LL178, L812LL178, L924LL178, L927LL178, L925LL178" \
      ", L357LL178, L753LL178, L945LL178, L679LL178, L470LL178, L679LL178, L736LL178" \
      ", L699LL178, L810LL178, L567LL178, L937LL178, L670LL178, L923LL178, L499LL178"

print(*re.findall(r'\+7\(812\)\d{3}-\d{2}.?\d{2}\b|\+7\(921\)\d{3}-\d{2}.?\d{2}\b', str))
