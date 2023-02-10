#! /usr/bin/python


# Импортируем модуль openpyxl
import openpyxl
import statistics

# Открываем на чтение рабочую книгу
wb = openpyxl.load_workbook("task_10-3.xlsx")
# Записываем в переменную все страницы рабочей книги
sheet = wb.sheetnames
# Записываем в переменную первую страницу
ws = wb[sheet[0]]
# пустой словарь
dct = {}
# Цикл по максимальной строке на странице
for i in range(ws.max_row):
    # Пустой список для записи двух ячеек
    z = []
    # Цикл по максимальной колонке на странице
    for j in range(ws.max_column):
        # Записываем две ячейки из строку в список
        x = ws.cell(row=i + 1, column=j + 1).value
        # Прверяем значение в ячейке, если есть, то
        if x is not None:
            # записываем в список, если нет, пропускаем
            z.append(x)
    # Берем из списка имя и удаляем его из списка
    y = z.pop(0)
    # имя это ключ в словаре, список цифр в значение
    dct[y] = z
for k, v in dct.items():
    m = [min(v), max(v), round(statistics.mean(v), 1), statistics.median(v)]
    dct[k] = m
dct = dict(sorted(dct.items()))
print(dct)

# Открываем на чтение рабочую книгу
wb = openpyxl.load_workbook("task_10-2.xlsx")
# Прверяем в книги, есть ли Лист3,
if 'Лист2' in wb.sheetnames:
    # если есть удаляем его
    wb.remove(wb["Лист2"])
# Создаём третию страницу в рабочей книге
wb.create_sheet("Лист2")
# Записываем в переменную все страницы рабочей книги
sheets = wb.sheetnames
# Переключаемся на третию страницу
ws = wb[sheets[1]]
# Счетчик строк

for k, v in dct.items():
    row = 1
    for i, j in enumerate(range(65, 70), 1):
        # ws[str(chr(i)) + str(row)] = k
        print(str(chr(i)) + str(j), "=", k)

        print(str(chr(i)) + str(j), "=", v[j - 1])
        # ws[str(chr(i)) + str(j)] = v[j - 1]
    row += 1

# Сохраняем все вычисления в файл
wb.save("task_10-3.xlsx")
