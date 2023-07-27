from os import getenv
from dotenv import load_dotenv
from etl.etl import ETL
from extractors.extractor_prix import ExtractorPrix
from transformers.transformer_prix import TransformerPrix
from loaders.loader_prix import LoaderPrix
from config.configs_prix import ROUTES_PRIX
from logger.main import Logger

load_dotenv()
URL = getenv("URL_PRIX")

class ETLPrix(ETL):
    def __init__(self):
        self.extracter = ExtractorPrix(URL,ROUTES_PRIX)
        self.tranformer = TransformerPrix()
        self.loader = LoaderPrix()
        self.data = None
    def extract(self):
        Logger.emit('Extracting data from Prix')
        self.data = self.extracter.extract()
    def transform(self):
        Logger.emit('Transforming data from Prix')
        self.data = self.tranformer.transform(self.data)
    def load(self):
        Logger.emit('Loading data from Prix')
        self.loader.load(self.data)
    def run(self):
        Logger.emit('Initalizing ETL for Prix')
        self.extract()
        self.transform()
        self.load()
        Logger.emit('Finishing ETL for Prix')
        