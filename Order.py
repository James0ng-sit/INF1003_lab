from Product import Product
from OrderLine import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_line: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_lines = OrderLine(product, quantity)
        self.__order_line.append(order_lines)

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.__order_line:
            total += order_line.calculate_subtotal()
        return total

    def display_information(self) -> None:
        print(f"OrderID: {self.__order_id}")
        for order_line in self.__order_line:
            order_line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")

    def remove_order_line(self, index: int) -> None:
        if index < 0 or index >= len(self.__order_line):
            print("Invalid line Number")
        else:
            self.__order_line.pop(index)

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_line)
