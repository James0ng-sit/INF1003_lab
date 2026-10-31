from Product import Product
from CanBeDownloaded import CanBeDownloaded

class DigitalProduct(Product, CanBeDownloaded):

    def __init__(self, product_id, name, price, stock, download_size, history=None):
        super().__init__ (product_id, name, price, stock, history)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"download size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally"

    def calculate_download_cost(self):
        return self.__download_size * 0.01
        