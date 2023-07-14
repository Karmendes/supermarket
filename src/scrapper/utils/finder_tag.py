from bs4 import BeautifulSoup


class Tagger:
    def __init__(self, response=None):
        self.response = response
        self.soup = BeautifulSoup(self.response.content, "html.parser")
    def get_all_tags(self, tag, **kwargs):
        return self.soup.find_all(tag, **kwargs)
    def get_single_tag(self, tag, **kwargs):
        return self.soup.find(tag, **kwargs)
