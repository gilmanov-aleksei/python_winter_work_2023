#! /usr/bin/python

from datetime import date
import locale

# d1 = datetime.strptime('10 02 2023 20:35', '%d %m %Y %H:%M')
# d2 = datetime.strptime('10 02 2023 20:37', '%d %m %Y %H:%M')
# d = d2 - d1

print(locale.setlocale(locale.LC_ALL, 'ru'))
print(locale.getlocale())
# d = date(2023, 2, 10)
# print(d.strftime("%a %d, %b %Y"))
birthday = date(1979, 9, 30)
print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))
