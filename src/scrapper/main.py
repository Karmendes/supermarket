import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, url = None):
        self.url = url
        self.response = None
        self.soup = None
        self.fetch_page()
    def fetch_page(self):
        self.response = requests.get(self.url,timeout=10)
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.content, "html.parser")
        else:
            print("Erro ao acessar a página:", self.response.status_code)
    def get_all_tags(self,tag,xpath,object_ = None):
        if object_ is None:
            return self.soup.find_all(tag,xpath)
        return object_.find_all(tag,xpath)
    def get_single_tag(self,tag,xpath,obj= None):
        if obj is None:
            return self.soup.find(tag,xpath)
        return obj.find(tag,xpath)