from abc import ABC, abstractmethod

class CanbeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass