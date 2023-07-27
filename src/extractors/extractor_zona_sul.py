from scrapper.scrap_zona_sul import ZonaSulScraper
from extractors.main import Extractor
from utils.main import generate_list

class ExtractorZonaSul(Extractor):
    def __init__(self,url,config):
        self.url = url
        self.config = config
        self.list_routes = generate_list(config)
        self.data = []
    def extract(self):
        for route in self.list_routes:
            url = self.url + route
            scrapper = ZonaSulScraper(url)
            self.data.append(scrapper.scrap_data())
        return self.data