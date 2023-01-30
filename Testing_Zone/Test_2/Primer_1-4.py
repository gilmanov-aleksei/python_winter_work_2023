y = int(input("Введите год: "))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f"Год {y} високосный")
else:
    print(f"Год {y} не високосный")

if y % 400 == 0:
    print("високосный")

