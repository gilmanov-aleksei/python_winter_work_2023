#! /usr/bin/python

# Задача 22-3

import keyword
from flashtext.keyword import KeywordProcessor


def replace_words(string):
    kw_list = keyword.kwlist
    keyword_processor = KeywordProcessor()
    for i in kw_list:
        keyword_processor.add_keyword(i, '<kw>')
    new_string = keyword_processor.replace_keywords(string)
    return new_string


text = 'if x == 2: and  as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))