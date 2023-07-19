from abc import ABC, abstractmethod

class Scrapper(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def scrap_data(self):
        pass