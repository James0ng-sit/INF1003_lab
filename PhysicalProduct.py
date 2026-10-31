from Product import Product
from CanbeShipped import CanbeShipped


class PhysicalProduct(Product, CanbeShipped):
    def __init__(self, product_id, name, price, stock, weight, history=None):
        super().__init__ (product_id, name, price, stock, history)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")
    
    def get_fulfilment_info(self):
        return "This product requires physical shipping"

    def calculate_shipping_cost(self):
        return self.__weight * 0.5



    