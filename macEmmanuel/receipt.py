class Item:
    def __init__(self, item_name, price, quantity):
        self.__price = price
        self.__quantity = quantity
        self.__item_name = item_name

    def calculate_total(self):
        return self.__price * self.__quantity

    def __str__(self) -> str:
        return self.__item_name + "\t\t\t" + self.__quantity + "\t\t" + self.__price + "\t\t" + self.calculate_total
