from datetime import datetime
import pandas as pd



class ReadMapReduce:
    def __init__(self):
        pass
    def read(self,data:list):
        list_data = [pd.DataFrame(x) for x in data]
        return pd.concat(list_data)





class DataManipulator:
    def __init__(self,reader):
        self.reader = reader()
        self.data = None
        print("Instanciando classe de manipulação de dados")
    def read_data(self,data):
        self.data = self.reader.read(data)
    def join_columns(self,new_column,columns,sep,axis):
        self.data[new_column] = self.data[columns].agg(sep.join, axis=axis)
    def replace_pattern(self,column,pattern_old,pattern_new):
        self.data[column] = self.data[column].str.replace(pattern_old, pattern_new)
    def casting(self,column,form):
        self.data[column] = self.data[column].astype(form)
    def mark_timestamp(self,column = 'dh_extraction'):
        self.data[column] = datetime.now()
    def mark_source(self,source):
        self.data['source'] = source
    #return df_[['names','price','dh_extraction']]