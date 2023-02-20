#! /usr/bin/python

# st = "Числа 99, 272, 81 и 999 деляться на на 9"
# import re
# print(re.findall(r" \d{2},", st))

# st = "Широка страна моя родная"
# import re
# print(re.findall(r"\b\w+о\w+\b", st))

# import re
# string = "0abracadabra1"
# regex = r".a."
# print(re.findall(regex, string))

# import re
# string = "100 200 1134 321 999 299 1999 199"
# regex = r"\b1\d\d\b"
# print(re.findall(regex, string))
#
# string = "Косой косой косил траву на косе"
# import re
# # print(re.findall(r"\b\w+\b", string))
# print(re.findall(r"\b\w*[Кк]ос\w+\b", string))


string = "cat cut c#t caut ciat coot ct"
import re
print(re.findall(r"\bc[^au]t\b", string))
