from item import Item

class TestItem(TestCase):
    #given
    def test_calculate_total(self):
        #when
        item = Item("Puff Puff", 120, 2)
        #assert
        self.assertEqual(240, item.calculate_total())

    def test_to_string(self):
        item = Item("Puff Puff", 120, 2)
        expected = "Puff Puff" + "\t\t\t" + "120" + "\t\t" + "2" + "\t\t" + "240"
        self.assertEqual(item.__str__(), expected)
        print(item)