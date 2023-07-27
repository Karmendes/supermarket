from transformers.main import Transformer
from data_manipulator.main import DataManipulator,ReadMapReduce

class TransformerPrix(Transformer):
    def __init__(self):
        self.manipulator = DataManipulator(ReadMapReduce)
    # Read data
    def transform(self,data):
        self.manipulator.read_data(data)
        self.manipulator.mark_timestamp()
        self.manipulator.mark_source('Prix')
        return self.manipulator.data