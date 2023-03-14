#! /usr/bin/python

# Задача 22-3

import keyword
from flashtext.keyword import KeywordProcessor


def replace_words(string):
    # Получаем список всех ключевых слов Python
    kw_list = keyword.kwlist

    keyword_processor = KeywordProcessor()
    # Цикл, перебираем все ключевые слова
    for word in kw_list:
        # Добавляем ключевые слова в словарь для замены на <kw>
        keyword_processor.add_keyword(word, '<kw>')
    # Заменяем в строке все ключеве на <kw>
    new_string = keyword_processor.replace_keywords(string)
    return new_string


text = 'if x == 2: and  as assert print("x is 2") else print("x is not 2")'
print(replace_words(text))
