import item
from Cart import cart
from item import Item

cart_owners_name = "default"
def set_up_cart():
    global cart
    cart_owners_name = input("What is your name\n")
    Cart = cart(cart_owners_name)

def add_items_to_cart():
    more_items = "yes"
    while more_items == "yes":
        add_item_to_cart()
        more_items = input("Anything else? \n").lower()

def add_item_to_cart():
    item_name = input("What did " + cart_owners_name + " buy?\n")
    item_price = float(input("How much did the " + item_name + " cost\n"))
    item_quantity = int(input("How many " + item_name + " did" + cart_owners_name + " buy\n"))
    item = Item (item_name, item_price, item_quantity)
    Cart.add(item)

def display_invoice():
    print(cart)
    print("Your total bill is " + str(Cart.calculate_total_price()))

if __name__ == "__main__":
    set_up_cart()
    add_item_to_cart()
    add_items_to_cart()
    display_invoice()
