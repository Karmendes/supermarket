from os import getenv
from dotenv import load_dotenv
from etl.etl import ETL
from extractors.extractor_zona_sul import ExtractorZonaSul
from transformers.transformer_zona_sul import TransformerZonaSul
from loaders.loader_zona_sul import LoaderZonaSul
from config.configs_zona_sul import ROUTES_ZONA_SUL


load_dotenv()
URL = getenv("URL_ZONA_SUL")



class ETLZonaSul(ETL):
    def __init__(self):
        self.extracter = ExtractorZonaSul(URL,ROUTES_ZONA_SUL)
        self.tranformer = TransformerZonaSul()
        self.loader = LoaderZonaSul()
        self.data = None
    def extract(self):
        print('Extraindo dados do zona sul')
        self.data = self.extracter.extract()
    def transform(self):
        print('Transformando dados do zona sul')
        self.data = self.tranformer.transform(self.data)
    def load(self):
        print('Carregando dados do zona sul')
        self.loader.load(self.data)
    def run(self):
        print('Rodando pipeline dos dados do zona sul')
        self.extract()
        self.transform()
        self.load()
        print('Completando pipeline dos dados do zona sul')