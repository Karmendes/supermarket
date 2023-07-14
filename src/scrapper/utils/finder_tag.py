from bs4 import BeautifulSoup


class Tagger:
    def __init__(self, requester):
        self.response = requester.execute()
        self.soup = BeautifulSoup(self.response.content, "html.parser")
    def get_all_tags(self, tag, **kwargs):
        return self.soup.find_all(tag, **kwargs)
    def get_single_tag(self, tag, **kwargs):
        return self.soup.find(tag, **kwargs)
