from Product import Product
from CanbeShipped import CanbeShipped
from Supplier import Supplier


class PhysicalProduct(Product, CanbeShipped):
    SHIPPING_RATE = 0.5  # Shipping cost per kg
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float, history: list=None) -> None:
        super().__init__ (product_id, name, price, stock, supplier, history)
        self.__weight:float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print(f"Shipping cost: ${self.calculate_shipping_cost():.2f}")
    
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        return self.__weight * PhysicalProduct.SHIPPING_RATE 

    def to_dict(self) -> dict:
         storage = super().to_dict()
         storage["type"] = "physical"
         storage["weight"] = self.__weight
         return storage



    