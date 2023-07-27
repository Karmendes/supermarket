from scrapper.utils.finder_tag import Tagger
from scrapper.utils.requester import Getter
from scrapper.main import Scrapper



class ZonaSulScraper(Scrapper):
    def __init__(self, url):
        self.url = url
        self.scrapper = Tagger(Getter(self.url))
        self.data = {}
    def get_names(self):
        tag_names = self.scrapper.get_all_tags("span", class_="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body")
        self.data['names'] = [x.text for x in tag_names]
    def get_full_prices(self):
        tag_prices = self.scrapper.get_all_tags("span",
        class_="zonasul-zonasul-store-0-x-customPricePor vtex-difference__por fw7 f5 text-center flex justify-center")
        self.data['integer'] = [self.scrapper.get_single_tag("span",
        class_="zonasul-zonasul-store-0-x-currencyInteger", obj=x).text for x in tag_prices]
        self.data['decimal'] = [self.scrapper.get_single_tag("span",
        class_="zonasul-zonasul-store-0-x-currencyFraction", obj=x).text for x in tag_prices]
    def scrap_data(self):
        self.get_names()
        self.get_full_prices()
        return self.data

class ManagerZonaSulScrapper():
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
