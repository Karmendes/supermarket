from os import getenv
from dotenv import load_dotenv
from etl.etl import ETL
from extractors.extractor_zona_sul import ExtractorZonaSul
from transformers.transformer_zona_sul import TransformerZonaSul
from loaders.loader_zona_sul import LoaderZonaSul
from config.configs_zona_sul import ROUTES_ZONA_SUL
from logger.main import Logger


load_dotenv()
URL = getenv("URL_ZONA_SUL")



class ETLZonaSul(ETL):
    def __init__(self):
        self.extracter = ExtractorZonaSul(URL,ROUTES_ZONA_SUL)
        self.tranformer = TransformerZonaSul()
        self.loader = LoaderZonaSul()
        self.data = None
    def extract(self):
        Logger.emit('Extracting data from Zona Sul')
        self.data = self.extracter.extract()
    def transform(self):
        Logger.emit('Transforming data from Zona Sul')
        self.data = self.tranformer.transform(self.data)
    def load(self):
        Logger.emit('Loading data from Zona Sul')
        self.loader.load(self.data)
    def run(self):
        Logger.emit('Initalizing ETL for Zona Sul')
        self.extract()
        self.transform()
        self.load()
        Logger.emit('Finishing ETL from Zona Sul')