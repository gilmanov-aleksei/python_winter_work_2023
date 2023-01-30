#! /usr/bin/python

# n = inprut("Enter a word: ")
n = "ab18,c#2wc64-+*656fab=561xz!-baz35"

str_0 = set(''.join(s for s in n if s.isalpha()))
num_0 = set(''.join(s for s in n if s.isdigit()))
znak1 = set(''.join(s for s in n if not s.isdigit()))
znak2 = set(''.join(s for s in n if not s.isalpha()))
print(*num_0)
print(*str_0)
print(*znak1 & znak2)



