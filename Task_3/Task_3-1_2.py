#! /usr/bin/python

f1 = "Введите Фамилию (0 - Выход): "
z1 = "Введите ЗП: "
sr_zp = "Средняя зарплата на"
tov = "Товарищ "
mec = " - меценат, мы его считать не будем."
s_0 = "Список пуст, нам некого счтитать."
fio = []
zp = []
while True:
    print()
    f = str(input(f1))
    if f == "0":
        break
    z = int(input(z1))
    if z <= 0:
        print(tov, f, mec)
        continue
    fio.append(f)
    zp.append(z)
if len(zp):
    s_zp = sum(zp) / len(zp)
    print(sr_zp, len(zp), ":", s_zp)
else:
    print(s_0)
