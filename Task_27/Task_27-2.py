#! /usr/bin/python

# Задача 27-2
#
# Необходимо реализовать класс item, описывающий предмет, конструктор
# которого принимает три аргумента:
# name - название придмета
# price - цена предмета в рублях
# quantity - количество предметов
# При обращении к атрибуту name экземпляр класса item будет возвращать
# его название с заглавной буквы, а при обращении к атрибуту total -
# произведение цены предмета на его количество


class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name.title()

    @property
    def total(self):
        return self._price * self._quantity


if __name__ == "__main__":
    item1 = Item("ноуТбук", 55_000, 4)
    item2 = Item("смарТфон", 25_000, 7)

    print(item1.name)
    print(item1.total)
    print(item2.name)
    print(item2.total)
