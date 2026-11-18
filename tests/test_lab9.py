import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order
from DiscountStrategy import BulkDiscount, PercentageDiscount, StudentDiscount
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

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

class TestFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")

    def test_creates_physical(self):
        product = ProductFactory.create("physical", "G001", "Guitar", 125, 10, self.supplier, 5)
        self.assertIsInstance(product, PhysicalProduct)

    def test_creates_digital(self):
        product = ProductFactory.create("digital", "D001", "Photo Editor", 49.9, 100, self.supplier, 200)
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier)