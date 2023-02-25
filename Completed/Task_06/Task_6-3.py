#! /usr/bin/python

# n = inprut("Enter a word: ")
n = "ab18,c#2wc64-+*656fab=561xz!-baz35"
# Выводим на печать множество только отсартированых букв
print(* sorted(set(''.join(s for s in n if s.isalpha()))))

# Выводим на печать множество только отсартированых цифр
print(* sorted(set(''.join(s for s in n if s.isdigit()))))

# Собираем из двух множеств, в одно нет цифр, вдругом нет букв,
# Производим пересечение двух множеств.
# Выводим на печать отсартированые символы.
print(* sorted(set(''.join(s for s in n if not s.isdigit()))
        & set(''.join(s for s in n if not s.isalpha()))))



