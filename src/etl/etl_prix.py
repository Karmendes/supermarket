from os import getenv
from dotenv import load_dotenv
from etl.etl import ETL
from extractors.extractor_prix import ExtractorPrix
from transformers.transformer_prix import TransformerPrix
from loaders.loader_prix import LoaderPrix
from config.configs_prix import ROUTES_PRIX

load_dotenv()
URL = getenv("URL_PRIX")

class ETLPrix(ETL):
    def __init__(self):
        self.extracter = ExtractorPrix(URL,ROUTES_PRIX)
        self.tranformer = TransformerPrix()
        self.loader = LoaderPrix()
        self.data = None
    def extract(self):
        print('Extraindo dados do Prix')
        self.data = self.extracter.extract()
    def transform(self):
        print('Transformando dados Prix')
        self.data = self.tranformer.transform(self.data)
    def load(self):
        print('Carregando dados do Prix')
        self.loader.load(self.data)
    def run(self):
        print('Rodando pipeline dos dados do Prix')
        self.extract()
        self.transform()
        self.load()
        print('Completando pipeline dos dados do Prix')
        