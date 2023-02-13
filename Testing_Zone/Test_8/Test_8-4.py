#! /usr/bin/python


from string import ascii_letters
vowel = 'aeiouаеёиоуэюа'
letters = 'gahjрouрро12аио676'
print([x+'-Yes' if x in vowel else x+'-No' for x in letters])
# is_eng = [f'{ltr}-ДА' if ltr in ascii_letters else f'{ltr}-НЕТ' for ltr in letters]
