from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_connector.main import DataBaseConnector

class PostgreSQLConnector(DataBaseConnector):
    def __init__(self):
        super().__init__(self.user,self.pwd,self.host,self.port,self.database)
        self.engine = None
        self.session = None
        self.session_maker = None
    def connect(self):
        # Lógica específica para a conexão com o PostgreSQL
        self.engine = create_engine(
            f"postgresql://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.database}",
            **self.kwargs
        )
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
    def send_data(self,dataframe,table_name,**kwargs):
        dataframe.to_sql(table_name,self.session,**kwargs)
    def retrieve_data(self,query):
        raise NotImplementedError()