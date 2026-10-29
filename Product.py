class Product:
    def __init__(self, product_id, name, price, stock, history=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__history = history if history is not None else [stock]

    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Not enough stock. Current stock is", self.__stock)
        else:
            self.__stock = self.__stock + quantity
            self.__history.append(quantity)
            print(f"{self.__name} stock is now {self.__stock}.")

    def display_information(self):
        print(f"{self.__name:<15}{self.__price:>10.2f}{self.__stock:>8}   {self.__history}")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "history": self.__history
        }