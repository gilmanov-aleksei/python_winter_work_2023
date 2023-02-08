#! /usr/bin/python


# str1 = input("Введите первое слов: ")
# str2 = input("Введите слова через пробел: ")
s1 = 'питона'
s2 = 'поросенок титан итоги лавка погосут киношы'
glas = {'а': 0, 'у': 0, 'о': 0, 'ы': 0, 'и': 0, 'э': 0, 'я': 0, 'ю': 0, 'ё': 0, 'е': 0, }
gls1 = 0
sl1 = list(s1)
for i, j in enumerate(sl1):
    if j in glas:
        gls1 += 1
print('Слова, похожие на:', s1)
sl2 = s2.split()
lsl2 = len(sl2)
for i in sl2:
    sl3 = list(i)
    lsl3 = len(i)
    gls2 = 0
    #    print(i)
    if lsl2 <= lsl3 + 2 or lsl2 == lsl3:
        for c, v in enumerate(sl1):
            if v in glas:
                if c < lsl3 and sl3[c] in glas:
                    gls2 += 1
        if gls1 == gls2:
            print(''.join(map(str, sl3)))
