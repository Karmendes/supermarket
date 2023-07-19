from src.scrapper.utils.finder_tag import Tagger
from src.scrapper.utils.requester import Getter
from src.scrapper.main import Scrapper

class ScrapperPrix(Scrapper):
    def __init__(self, url):
        self.url = url
        self.scrapper = Tagger(Getter(self.url))
        self.data = {}
    def get_names(self):
        tag_names = self.scrapper.get_all_tags("div", class_="discount")
        self.data['names'] = [x.find('a')['title'] for x in tag_names]
    def get_full_prices(self):
        tag_prices = self.scrapper.get_all_tags("div", class_="price")
        self.data['prices'] = [x.find('span',class_ = 'newPrice').find('em').text for x in tag_prices]
    def scrap_data(self):
        print("Scraping dos dados do Zona Sul")
        self.get_names()
        self.get_full_prices()
        return self.data
if __name__ == '__main__':
    scrapper = ScrapperPrix('https://www.superprix.com.br/bebidas/cervejas')
    scrapper.get_names()
    scrapper.get_full_prices()