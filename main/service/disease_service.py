import json
from bson import ObjectId
import pymongo
import bson
import re

from ..model.Disease import Disease
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder 

class DiseaseService:

    def __init__(self):
        db = Database('epidemi')
        self.db = db.get_database()
        self.documento = self.db['enfermedades']

    def save_disease(self,enfermedad):
        try:
            self.documento.insert_one(enfermedad.get_disease_info())
            return True
        except:
            return False
    
    def get_all_diseases(self):
        diseases = []
        try:
            cursor = self.documento.find()
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                diseases.append(doc)
            return diseases
        except:
            return False
    
    def get_diseases_pagination(self,pag):
        diseases = []
        cursor = self.documento.find({}).skip(int(pag)*3).limit(3)
        for doc in cursor:
            doc['_id'] = JSONEncoder().encode(doc['_id'])
            diseases.append(doc)
        return diseases
    
    def get_all_diseases_count(self):
        cursor = self.documento.find({})
        total = 0
        for doc in cursor:
            total = total + 1
        return total

    def delete_disease(self,id):
        try:
            disease = self.documento.delete_one({"_id":ObjectId(id)})
            return True
        except:
            return False

    def get_disease(self,id):
        try:
            disease = self.documento.find_one(
                {
                    "_id":ObjectId(id)
                }
            )
            disease['_id'] = JSONEncoder().encode(disease['_id'])
            return disease
        except:
            return False
    
    def update_disease(self,id, disease):
        try:
            disease = self.documento.update_one(
                {
                    "_id":ObjectId(id)
                },
                {
                    "$set": disease.get_disease_info()
                }
            )
            return True
        except:
            return False

    def search_disease(self, name, pag):
        page = (int(pag)-1)*3
        print(page)
        diseases = []
        regx = re.compile(name, re.IGNORECASE)
        try:
            cursor = self.documento.find({'nombre_enfermedad':regx}).skip(page).limit(3)
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                diseases.append(doc)
            return diseases
        except:
            return False

