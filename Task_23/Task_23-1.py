#! /usr/bin/python

# Найдите длину наибольшей подстроки данной строки, которая
# является палиндромом.
# Например, дана строка 'aabbccddcc' тогда длиной подстроки с
# наибольшим палиндромом является 6 (подстрока 'ccddcc')

def find_long_palindrome(txt):
    max_len = []
    for i in range(len(txt)):
        for j in range(len(txt), i, -1):
            if len(max_len) > 0 and len(max_len[0]) >= j - i:
                break
            elif txt[i:j] == txt[i:j][::-1]:
                max_len.append(txt[i:j])
    max_len = max_len.sort()
    return max_len


str = 'aababcacdedcaceeefffeeeklmnonmlk'
flp = find_long_palindrome(str)
print(flp)  # ['aceeffea', 'mnonm', 'klk']


