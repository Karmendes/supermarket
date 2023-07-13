from src.etl.etl import ETL

class ETLPrix(ETL):
    def __init__(self):
        pass
    def extract(self):
        print('Extraindo dados do prix')
    def transform(self):
        print('Transformando dados do prix')
    def load(self):
        print('Carregando dados do prix')
    def run(self):
        print('Rodando pipeline dos dados do prix')
        self.extract()
        self.transform()
        self.load()
        print('Completando pipeline dos dados do prix')
        