#! /usr/bin/python

# import re
#
# text = 'abracadabra'
# # res = re.finditer(r"a", text)
# res = re.finditer(r"[^a]", text)
# for i in res:
#     print(i.group(), i.start(), i.end())

# import re
#
# text = "1 + 2222 * 3 - 7 / 2"
# # print(re.split(r"\s+", text))
# print(re.split(r"\D+", text))

import re

x = 5
print(re.findall(fr"{x}", '112233445566'))

res = '|'.join(str(i) for i in range(x))
print(re.findall(fr"{res}", '112233445566'))
