import json 
from bson import ObjectId
import pymongo

from ..model.Pacient import Pacient
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder

import re

class PacientService:

    def __init__(self):
        db = Database('epidemi')
        self.db = db.get_database()
        self.documento = self.db["pacientes"]

    def save_pacient(self, pacient):
        try:
            self.documento.insert_one(pacient.get_pacient_info())
            return True
        except:
            return False
    
    def get_all_pacients(self):
        pacients = []
        try:
            cursor = self.documento.find()
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                pacients.append(doc)
            return pacients
        except:
            return False
    
    def get_pacients_pagination(self,pag):
        pacients = []
        cursor = self.documento.find({}).skip(int(pag)*3).limit(3)
        for doc in cursor:
            doc['_id'] = JSONEncoder().encode(doc['_id'])
            pacients.append(doc)
        return pacients
    
    def get_all_pacients_count(self):
        cursor = self.documento.find({})
        total = 0
        for doc in cursor:
            total = total + 1
        return total

    def delete_pacient(self,id):
        try:
            pac = self.documento.delete_one({"_id":ObjectId(id)})
            return True
        except:
            return False

    def get_pacient(self,id):
        try:
            pacient = self.documento.find_one(
                {
                    "_id":ObjectId(id)
                }
            )
            pacient['_id'] = JSONEncoder().encode(pacient['_id'])
            return pacient
        except:
            return False
    
    def update_pacient(self,id, pacient):
        try:
            pacient = self.documento.update_one(
                {
                    "_id":ObjectId(id)
                },
                {
                    "$set": pacient.get_pacient_info()
                }
            )
            return True
        except:
            return False

    def search_pacient(self, name, pag):
        page = (int(pag)-1)*3
        pacients = []
        regx = re.compile(name, re.IGNORECASE)
        try:
            cursor = self.documento.find({'nombre':regx}).skip(page).limit(3)
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                pacients.append(doc)
            return pacients
        except:
            return False
