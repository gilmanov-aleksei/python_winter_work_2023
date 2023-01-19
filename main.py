# ------
x = int(input("Введите целое число: "))
y = int(input("Введите целое число: "))

try:
    x = int(x)
    y = int(y)

    res = x / y
except ZeroDivisionError:
    print("На 0 делить нельзя!")
except ValueError:
    print("Одно или несколько значений не число")

else:
    print("Исключений не произошло")