from loaders.main import Loaders
from db_connector.postgres_connector import PostgreSQLConnector
from utils.main import generate_credentials

USER,PWD,HOST,PORT,DATABASE = generate_credentials()


class LoaderPrix(Loaders):
    def __init__(self):
        self.db_conn = PostgreSQLConnector(USER,PWD,HOST,PORT,DATABASE)
    def load(self,data):
        self.db_conn.send_data(data,'tb_prix',if_exists='append',index = False,schema = 'staging')