from abc import ABC,abstractmethod

class Loaders(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def load(self,data):
        pass