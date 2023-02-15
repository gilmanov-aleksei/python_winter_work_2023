#! /usr/bin/python

while True:
    s = input("Введите целое число: ")
    try:
        n = int(s)
    except:
        try:
            n = float(s)
        except:
            print("Это не вещественное число")
            print("Повторите ввод!")
        else:
            print(f"Вещественно число: {n}")
            break
        print("Вы вели не целое число")
        print("Повторите ввод!")
    else:
        print(f"Вы вели число: {s}")
        break

