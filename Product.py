class Product:

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.__history = [stock]

    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Not enough stock. Current stock is", self.__stock)
        else:
            self.__stock = self.__stock + quantity
            self.__history.append(quantity)
            print(f"{self.__name} stock is now {self.__stock}.")

    def display_information(self):
            print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

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