from Item import Item


class Cart:
    def __init__(self, owner_name):
        self.owner_name= owner_name
        self.items=[]
    def add(self,item):
        self.items.append(item)
        
        

    


        