from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Order import Order
from DiscountStrategy import BulkDiscount, PercentageDiscount

supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")
guitar = PhysicalProduct("G001", "Guitar", 125, 10, supplier, 5)

order = Order("O1", BulkDiscount(200, 20))
order.add_order_line(guitar, 2)
print(order.calculate_total())

order.set_discount(PercentageDiscount(10))
print(order.calculate_total())