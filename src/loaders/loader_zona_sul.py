from src.loaders.main import Loaders
from src.db_connector.postgres_connector import PostgreSQLConnector

USER = 'datalake'
PWD = 'datalake'
DATABASE = 'datalake'
PORT = 5432
HOST = 'localhost'


class LoaderZonaSul(Loaders):
    def __init__(self):
        self.db_conn = PostgreSQLConnector(USER,PWD,HOST,PORT,DATABASE)
    def load(self,data):
        self.db_conn.send_data(data,'tb_zona_sul',if_exists='append',index = False,schema = 'staging')
