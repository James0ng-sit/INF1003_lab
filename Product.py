from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, history: list = None) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price:float = price
        self.__stock:int = stock
        self.__supplier: Supplier = supplier
        self.__history: list = history if history is not None else [stock]

    def update_stock(self, quantity: int) -> bool:
        if self.__stock + quantity < 0:
            print("Not enough stock. Current stock is", self.__stock)
            return False
        else:
            self.__stock = self.__stock + quantity
            self.__history.append(quantity)
            print(f"{self.__name} stock is now {self.__stock}.")
            return True

    def display_information(self) -> None:
        print(f"{self.__name:<15}{self.__price:>10.2f}{self.__stock:>8}   {self.__history}")

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self._get_price

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def to_dict(self) -> dict:
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "history": self.__history
        }
    @abstractmethod  
    def get_fulfilment_info(self) -> str:   
        pass 