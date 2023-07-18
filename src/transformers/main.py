from abc import ABC,abstractmethod

class Transformer(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def transform(self,data):
        pass