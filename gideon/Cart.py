from item import item

class Cart:
    def __init__(self, owners_name):
        self.owners_name = owners_name
        self.items = []

    def add(self, Item):
        self.items.append(item)

    def calculate_total_price(self):
        total = 0
        for item in self.items:
            total += item.calculate_total()
        return total

    def calculate_vat_of(self, percent):
        return self.calculate_total_price * (percent/100.0)
    
    def __str__(self):
        string_to_return = " "
        for item in self.items:
            string_to_return += item.__str__() + "\n"
        return string_to_return
        
