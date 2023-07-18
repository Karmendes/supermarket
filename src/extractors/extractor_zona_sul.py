from src.scrapper.scrap_zona_sul import ZonaSulScraper
from src.extractors.main import Extractor


class ExtractorZonaSul(Extractor):
    def __init__(self,url,config):
        self.url = url
        self.config = config
        self.list_routes = self.generate_list()
        self.data = []
    def generate_list(self):
        routes = []
        for chave, valores in self.config.items():
            for valor in valores:
                routes.append(f"{chave}/{valor}")
        return routes
    def extract(self):
        for route in self.list_routes:
            url = self.url + route
            scrapper = ZonaSulScraper(url)
            self.data.append(scrapper.scrap_data())
        return self.data