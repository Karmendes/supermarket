from src.scrapper.scrap_prix import PrixScrapper
from src.extractors.main import Extractor
from src.utils.main import generate_list


class ExtractorPrix(Extractor):
    def __init__(self,url,config):
        self.url = url
        self.config = config
        self.list_routes = generate_list(self.config)
        self.data = []
    def extract(self):
        for route in self.list_routes:
            url = self.url + route
            scrapper = PrixScrapper(url)
            self.data.append(scrapper.scrap_data())
        return self.data