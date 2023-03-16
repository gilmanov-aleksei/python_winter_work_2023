#! /usr/bin/python

import keyword
import re


def replace_words(txt):
    # Получаем список всех ключевых слов Python
    words = keyword.kwlist
    # Регулярное выражение, которое будет находить целые слова
    pattern = r'\b(' + '|'.join(words) + r')\b'
    # Заменяем все целые слова в тексте на '<kw>'
    replaced_txt = re.sub(pattern, '<kw>', txt)
    return replaced_txt


text = 'if x == 2: and  as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))
