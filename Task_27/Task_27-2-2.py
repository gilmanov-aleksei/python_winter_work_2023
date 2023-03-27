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

    def get_name(self):
        return self._name.title()

    def total(self):
        return self._price * self._quantity

    def prn_items(self):
        return print(f"Наименование: {self.get_name()}\n  Общая цена: {self.total()} Руб.")

if __name__ == "__main__":
    item1 = Item("ноуТбук", 55_000, 4)
    item2 = Item("смарТфон", 25_000, 7)

    # Ноутбук
    print(f"Наименование:", item1.get_name())
    # 220000
    print(f"  Общая цена:", item1.total(), "Руб.")
    # Смартфон
    print(f"Наименование:", item2.get_name())
    # 175000
    print(f"  Общая цена:", item2.total(), "Руб.")
    print()
    # Ноутбук - 220000
    item1.prn_items()
    # Смартфон - 175000
    item2.prn_items()


