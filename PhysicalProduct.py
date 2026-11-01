from Product import Product
from CanbeShipped import CanbeShipped


class PhysicalProduct(Product, CanbeShipped):
    SHIPPING_RATE = 0.5  # Shipping cost per kg
    def __init__(self, product_id, name, price, stock, weight, history=None):
        super().__init__ (product_id, name, price, stock, history)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print(f"Shipping cost: ${self.calculate_shipping_cost():.2f}")
    
    def get_fulfilment_info(self):
        return "This product requires physical shipping"

    def calculate_shipping_cost(self):
        return self.__weight * PhysicalProduct.SHIPPING_RATE 

    def to_dict(self):
         storage = super().to_dict()
         storage["type"] = "physical"
         storage["weight"] = self.__weight
         return storage



    