import os
from py2neo import Graph, Node, Relationship

class DataGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur_dir, 'data/data.csv')
        self.g = Graph("bolt://localhost:7687", auth=("neo4j", "11111111"))

    def read_nodes(self):
        
