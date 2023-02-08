#! /usr/bin/python

# Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв:
# G>C; C>G; T>A; A>T
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК, для этого постройте словарь для замены букв.
# Например:
# Вход:GGCTAA Результат: CCGATT


def dna_to_rnk(dna):
    #
    rnk = ""
    #
    for k in dna:
        #
        rnk += ddna.get(k)
    #
    return rnk
#
ddna = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'T'
}
#
dnk = ""
#
sdnk = str(input("Enter DNA letters: ")).upper()
#
keys = ddna.keys()
#
for i in sdnk:
    #
    if i in keys:
        #
        dnk += ddna.get(i)
# dnk = 'GGCTAA'
#
print(dnk)
#
print("-" * len(dnk))
#
print(dna_to_rnk(dnk))
