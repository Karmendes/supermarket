from os import getenv
from dotenv import load_dotenv
from src.etl.etl import ETL
from src.scrapper.scrap_zona_sul import ScrapperZonaSul
from src.bigquery.bq_connector import BigQueryConnector
from src.data_manipulator.main import DataManipulator

load_dotenv()
URL = getenv("URL_ZONA_SUL")




class ETLZonaSul(ETL):
    def __init__(self):
        self.extracter = ScrapperZonaSul(URL)
        self.manipulator = DataManipulator()
        self.loader = BigQueryConnector()
    def extract(self):
        print('Extraindo dados do zona sul')
        self.extracter.scrap_data()
    def transform(self):
        print('Transformando dados do zona sul')
        self.manipulator.manipulate_data()
    def load(self):
        print('Carregando dados do zona sul')
        self.loader.send_data()
    def run(self):
        print('Rodando pipeline dos dados do zona sul')
        self.extract()
        self.transform()
        self.load()
        print('Completando pipeline dos dados do zona sul')