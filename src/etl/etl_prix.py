from os import getenv
from dotenv import load_dotenv
from src.etl.etl import ETL
from src.extractors.extractor_prix import ExtractorPrix
from src.transformers.transformer_prix import TransformerPrix
#from src.loaders.loader_zona_sul import LoaderZonaSul
from src.config.configs_prix import ROUTES_PRIX

load_dotenv()
URL = getenv("URL_PRIX")

class ETLPrix(ETL):
    def __init__(self):
        self.extracter = ExtractorPrix(URL,ROUTES_PRIX)
        self.tranformer = TransformerPrix()
        #self.loader = LoaderZonaSul()
        self.data = None
    def extract(self):
        self.data = self.extracter.extract()
    def transform(self):
        self.data = self.tranformer.transform(self.data)
    def load(self):
        print('Carregando dados do prix')
    def run(self):
        print('Rodando pipeline dos dados do prix')
        self.extract()
        self.transform()
        self.load()
        print('Completando pipeline dos dados do prix')
        