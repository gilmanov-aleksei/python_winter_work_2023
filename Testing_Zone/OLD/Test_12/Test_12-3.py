#! /usr/bin/python

import re

# text = 'first second'
# print(re.sub(r"(first) (second)", r'\2 \1', text))

# text = 'Гильманов Алексей Гаптрауфович'
# print(re.sub(r"(Гильманов) (Алексей) (Гаптрауфович)", r'\2 \3 \1', text))

# import re
#
# text = 'Программы на Java транслируются в байт код java,' \
#        'выполняемый виртуальной машиной Java (JVM) программой,' \
#        'обрабатывающей байтовый код и передающей инструкции оборудованию как интерпретатор.'
# res = re.sub(r'Java', r'Python', text, count=2, flags=re.I)
# print(res)

# import re
#
# text = '123 first 234 second'
# print(re.findall(r"\d+(\w+)", text))

import re

text = 'Миша:123 Коля:234 Сеня:345'
res = re.findall(r"(\w+):(\d+)", text)
print(res)
