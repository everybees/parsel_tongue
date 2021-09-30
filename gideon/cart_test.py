from Cart import Cart
from item import Item

class TestCart(TestCase):
    def test_add(self):
        Cart = cart("Gid")
        self.assertEqual(0, len(Cart.items))
        item = Item("Pampers", 230, 4)
        Cart.add(item)
        self.assertEqual(1, len(Cart.items))

    def test_constructor(self):
        Cart = cart("Gid")
        self.assertEqual("Kim", Cart.owners_name)

    def test_calculate_total_price(self):
        Cart = cart("Gid")
        self.assertEqual(0, len(Cart.items))
        item = Item("Pampers", 230, 4)
        Cart.add(item)
        self.assertEqual(2, len(Cart.items))
        self.assertEqual(160, Cart.calculate_total_price())