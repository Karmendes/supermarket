from src.scrapper.utils.finder_tag import Tagger
from src.scrapper.utils.requester import Getter




class ZonaSulScraper:
    def __init__(self, url):
        self.url = url
        self.getter = Getter(self.url)
        self.response = self.getter.execute()
        self.scrapper = Tagger(self.response)
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
        print("Scraping dos dados do Zona Sul")
        self.get_names()
        self.get_full_prices()
        return self.data