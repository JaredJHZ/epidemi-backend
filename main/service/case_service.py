import json
from bson import ObjectId
import pymongo

from ..model.Case import Case
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder 
import re

class CaseService:

    def __init__(self):
        db = Database('epidemi')
        self.db = db.get_database()
        self.documento = self.db['casos']
    
    def save_case(self,caso):
        try:
            self.documento.insert_one(caso.get_case_info())
            return True
        except:
            return False

    def get_all_cases(self):
        cases = []
        try:
            cursor = self.documento.find()
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                cases.append(doc)
            return cases
        except:
            return False
    
    def get_cases_pagination(self,pag):
        cases = []
        cursor = self.documento.find({}).skip(int(pag)*5).limit(5)
        for doc in cursor:
            doc['_id'] = JSONEncoder().encode(doc['_id'])
            cases.append(doc)
        return cases
    
    def get_all_cases_count(self):
        cursor = self.documento.find({})
        total = 0
        for doc in cursor:
            total = total + 1
        return total

    def delete_case(self,id):
        try:
            case = self.documento.delete_one({"_id":ObjectId(id)})
            return True
        except:
            return False

    def get_case(self,id):
        try:
            case = self.documento.find_one(
                {
                    "_id":ObjectId(id)
                }
            )
            case['_id'] = JSONEncoder().encode(case['_id'])
            return case
        except:
            return False
    
    def update_case(self,id, case):
        try:
            case = self.documento.update_one(
                {
                    "_id":ObjectId(id)
                },
                {
                    "$set": case.get_case_info()
                }
            )
            return True
        except:
            return False

    def search_case(self, paciente, pag):
        page = (int(pag)-1)*3
        cases = []
        regx = re.compile(paciente, re.IGNORECASE)
        try:
            cursor = self.documento.find({'numero_expediente':regx}).skip(page).limit(3)
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                cases.append(doc)
            return cases
        except:
            return False
    
    def search_case_by_name(self, paciente, pag):
        page = (int(pag)-1)*3
        cases = []
        regx = re.compile(paciente, re.IGNORECASE)
        try:
            cursor = self.documento.find({'nombre_paciente':regx}).skip(page).limit(3)
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                cases.append(doc)
            return cases
        except:
            return False
