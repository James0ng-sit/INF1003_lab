import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order
from DiscountStrategy import BulkDiscount

class TestDiscounts(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")
        self.guitar = ProductFactory.create("physical", "G001", "Guitar", 125, 10, self.supplier, 5)

    def test_bulk_discount(self):
        order = Order("O1", BulkDiscount(200, 20))
        order.add_order_line(self.guitar, 2)
        self.assertEqual(230, order.calculate_total())