class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
       def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Error: not enough stock.")
        else:
            self.__stock = self.__stock + quantity
            def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")