from abc import ABC, abstractmethod
import requests

class Requester(ABC):
    def __init__(self, url=None):
        self.url = url
    @abstractmethod
    def execute(self):
        pass
class Getter(Requester):
    def execute(self):
        return requests.get(self.url, timeout=10)
class Postter(Requester):
    def execute(self):
        return requests.post(self.url, timeout=10)