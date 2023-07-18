from src.loaders.main import Loaders
from src.db_connector.sqlite_connector import SQLiteConnector

USER = 'lucas'
PWD = 'karmendes'
DATABASE = 'datalake'
PORT = 5555
HOST = 'localhost'


class LoaderZonaSul(Loaders):
    def __init__(self):
        self.db_conn = SQLiteConnector(USER,PWD,HOST,PORT,DATABASE)
    def load(self,data):
        self.db_conn.send_data(data,'tb_stg_zona_sul',if_exists='append',index = False)
