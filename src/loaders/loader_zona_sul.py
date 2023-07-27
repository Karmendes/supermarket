from loaders.main import Loaders
from db_connector.postgres_connector import PostgreSQLConnector
from utils.main import generate_credentials


USER,PWD,HOST,PORT,DATABASE = generate_credentials()


class LoaderZonaSul(Loaders):
    def __init__(self):
        self.db_conn = PostgreSQLConnector(USER,PWD,HOST,PORT,DATABASE)
    def load(self,data):
        self.db_conn.send_data(data,'tb_zona_sul',if_exists='append',index = False,schema = 'staging')
