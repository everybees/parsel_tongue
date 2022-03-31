from unittest import TestCase

from macEmmanuel.receipt import Item


class TestItem(TestCase):
    def test_calculate_total(self):
        # Given
        item = Item()
        # Condition
        total = item.calculate_total();

        # When
        self.assertEqual("Kim", item.__str__())
