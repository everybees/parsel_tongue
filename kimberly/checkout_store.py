

class Item:
    def __init__(self, name, price, quantity):
        self.__name=name
        self.__price=price
        self.__quantity=quantity

    def calculate_total(self):
        return self.__price*self.__quantity    


    def __init__(self):
        return self.__name + "\t\t\t" + str(self.__price) + "\t\t" +str(self.__quantity) + "\t\t" + str(self.calculate_total) ;
        