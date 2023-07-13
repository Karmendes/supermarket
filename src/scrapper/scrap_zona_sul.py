from src.scrapper.main import Scrapper


class ScrapperZonaSul():
    def __init__(self,url):
        self.url = url
        self.scrapper = Scrapper(self.url)
        self.data = {}
    def get_names(self):
        tag_names = self.scrapper.get_all_tags("span",{"class":"vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"})
        self.data['names'] = [x.text for x in tag_names]
    def get_full_prices(self):
        tag_prices = self.scrapper.get_all_tags("span",
        {"class":"zonasul-zonasul-store-0-x-customPricePor vtex-difference__por fw7 f5 text-center flex justify-center"})
        self.data['integer'] = [self.scrapper.get_single_tag("span",
        {"class":"zonasul-zonasul-store-0-x-currencyInteger"},x).text for x in tag_prices]
        self.data['decimal'] = [self.scrapper.get_single_tag("span",
        {"class":"zonasul-zonasul-store-0-x-currencyFraction"},x).text for x in tag_prices]
    def scrap_data(self):
        print("Scraping dos dados do zona sul")
        self.get_names()
        self.get_full_prices()
        return self.data