from Product import Product
from CanBeDownloaded import CanBeDownloaded
from Supplier import Supplier

class DigitalProduct(Product, CanBeDownloaded):
    DOWNLOAD_RATE = 0.01  # Download cost per MB

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float, history: list=None) -> None:
        super().__init__ (product_id, name, price, stock, supplier, history)
        self.__download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"download size: {self.__download_size} MB")
        print(f"Download cost: ${self.calculate_download_cost():.2f}")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally"

    def calculate_download_cost(self) -> float:
        return self.__download_size * DigitalProduct.DOWNLOAD_RATE

    def to_dict(self) -> dict:
         storage = super().to_dict()
         storage["type"] = "digital"
         storage["download_size"] = self.__download_size
         return storage

        