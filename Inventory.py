class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            for product is self.__products:
                product.display_information()