import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order
from DiscountStrategy import BulkDiscount, PercentageDiscount, StudentDiscount

class TestDiscounts(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")
        self.guitar = ProductFactory.create("physical", "G001", "Guitar", 125, 10, self.supplier, 5)

    def test_bulk_discount(self):
        order = Order("O1", BulkDiscount(200, 20))
        order.add_order_line(self.guitar, 2)
        self.assertEqual(230, order.calculate_total())

    def test_set_discount(self):
        order = Order("O1", BulkDiscount(200, 20))
        order.add_order_line(self.guitar, 2)
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(225, order.calculate_total())

    def test_student_discount(self):
        order = Order("O1", StudentDiscount())
        order.add_order_line(self.guitar, 2)
        self.assertEqual(237.5, order.calculate_total())