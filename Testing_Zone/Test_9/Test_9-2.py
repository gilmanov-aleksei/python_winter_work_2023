#! /usr/bin/python

while True:
    try:
        s = int(input("Введите целое число, 0 - Выход: "))
    except:
        print("Вы вели не целое число")
        print("Повторите ввод!")
    else:
        if s == 0:
            break
        else:
            print(s)
            print("Повторите ввод!")
    finally:
        print()
