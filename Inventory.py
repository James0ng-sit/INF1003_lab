class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def display_all(self):
        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            print(f"{'Name':<15}{'Price':>10}{'Stock':>8}   History")
            print("-" * 55)
            for product in self.__products:
                product.display_information()
            
    def search_product(self, name):
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                return product
        return None

    def to_list(self):
        return [product.to_dict() for product in self.__products]