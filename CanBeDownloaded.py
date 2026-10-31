from abc import ABC, abstractmethod

class CanBeDownloaded(ABC):
    @abstractmethod
    def calculate_download_cost(self):
        pass

