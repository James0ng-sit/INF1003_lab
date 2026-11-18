import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order
from DiscountStrategy import BulkDiscount, PercentageDiscount, StudentDiscount
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from OrderLine import OrderLine

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

class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")
        self.guitar = ProductFactory.create("physical", "G001", "Guitar", 125, 10, self.supplier, 5)

    def test_price_must_be_positive(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "G002", "Drum", 0, 10, self.supplier, 5)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "G002", "Drum", 100, -1, self.supplier, 5)

    def test_digital_follows_same_rules(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D002", "App", 10, -1, self.supplier, 50)

    def test_zero_stock_is_allowed(self):
        product = ProductFactory.create("physical", "G003", "Bass", 100, 0, self.supplier, 5)
        self.assertEqual("Bass", product.get_name())

    def test_quantity_must_be_positive(self):
        with self.assertRaises(ValueError):
            OrderLine(self.guitar, 0)