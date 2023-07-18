from abc import abstractmethod

class DataBaseConnector():
    def __init__(self,user,pwd,host,port,database,**kwargs):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port
        self.database = database
        self.kwargs = kwargs
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def send_data(self,dataframe,table_name,**kwargs):
        pass
    @abstractmethod
    def retrive_data(self):
        pass