from src.etl.etl import ETL
from src.scrapper.scrap_zona_sul import ScrapperZonaSul
from src.bigquery.bq_connector import BigQueryConnector
from src.data_manipulator.main import DataManipulator



class ETLZonaSul(ETL):
    def __init__(self):
        self.extracter = ScrapperZonaSul()
        self.manipulator = DataManipulator()
        self.loader = BigQueryConnector()
    def extract(self):
        print('Extraindo dados do zona sul')
        self.extracter.scrap_date()
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