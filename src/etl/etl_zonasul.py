from os import getenv
from dotenv import load_dotenv
from src.etl.etl import ETL
from src.extractors.extractor_zona_sul import ExtractorZonaSul
from src.transformers.transformer_zona_sul import TransformerZonaSul
from src.loaders.loader_zona_sul import LoaderZonaSul
from src.config.configs_zona_sul import ROUTES_ZONA_SUL


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