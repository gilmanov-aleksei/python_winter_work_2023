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
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name.title()

    def total(self):
        return self.price * self.quantity

        # def prn_items(self):
        #     return print(f"Наименование: {self.get_title()}\n  Общая цена: {self.get_total()}")


if __name__ == "__main__":
    item1 = Item("ноутбук", 55000, 4)
    item2 = Item("смартфон", 25000, 7)

    # Ноутбук
    print(f"Наименование:", item1.get_name())
    # 220000
    print(f"  Общая цена:", item1.total())
    # Смартфон
    print(f"Наименование:", item2.get_name())
    # 175000
    print(f"  Общая цена:", item2.total())

    # Ноутбук - 220000
    # item1.prn_items()
    # Смартфон - 175000
    # item2.prn_items()
