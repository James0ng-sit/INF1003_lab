from Product import Product


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight, history=None):
        super().__init__ (product_id, name, price, stock, history)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    