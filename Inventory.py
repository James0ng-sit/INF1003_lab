from Product import Product


class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def display_all(self) -> None:
        if len(self.__products) == 0:
            print("Inventory is empty.")
        else:
            print(f"{'Name':<15}{'Price':>10}{'Stock':>8}   History")
            print("-" * 55)
            for product in self.__products:
                product.display_information()
            
    def search_product(self, name: str) -> Product | None:
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
            return product
        return None

    def to_list(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]