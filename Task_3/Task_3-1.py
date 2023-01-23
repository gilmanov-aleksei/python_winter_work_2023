#! /usr/bin/python

f1 = "Введите Фамилию (0 - Выход): "
z1 = "Введите ЗП (0 - Выход): "
sr_zp = "Средняя зарплата на"
s_0 = "Список пуст"
fio = []
zp = []
while True:
    f = str(input(f1))
    if f == "0":
        break
    z = int(input(z1))
    if z == 0:
        break
    fio.append(f)
    zp.append(z)
if len(zp):
    s_zp = sum(zp) / len(zp)
    print(sr_zp, len(zp), ":", s_zp)
else:
    print(s_0)
