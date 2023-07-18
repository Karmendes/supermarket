from src.transformers.main import Transformer
from src.data_manipulator.main import DataManipulator,ReadMapReduce

class TransformerZonaSul(Transformer):
    def __init__(self):
        self.manipulator = DataManipulator(ReadMapReduce)
    # Read data
    def transform(self,data):
        self.manipulator.read_data(data)
        self.manipulator.join_columns('price',['integer','decimal'],',',1)
        self.manipulator.replace_pattern('price',',','.')
        self.manipulator.casting('price',float)
        self.manipulator.mark_timestamp()
        self.manipulator.mark_source('Zona Sul')
        return self.manipulator.data
