import pymongo

class Database:
    def __init__(self, name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[name]

    def get_database(self):
        return self.db