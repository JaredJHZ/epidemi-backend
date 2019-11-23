import json
from bson import ObjectId
import pymongo

from ..model.User import User
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder 

import re

class UserService:

    def __init__(self):
        db = Database('epidemi')
        self.db = db.get_database()
        self.documento = self.db["usuarios"]

    def save_user(self, user):
        try:
            self.documento.insert_one(user.getUser())
            return True
        except:
            return False 

    def get_all_users_count(self):
        cursor = self.documento.find({}, {'password':0})
        total = 0
        for doc in cursor:
            total = total + 1
        return total

    def get_users_pagination(self,pag):
        users = []
        cursor = self.documento.find({},{'password':0}).skip(int(pag)*3).limit(3)
        for doc in cursor:
            doc['_id'] = JSONEncoder().encode(doc['_id'])
            users.append(doc)
        return users
    
    def delete_user(self, id):
        try:
            self.documento.delete_one({"_id":ObjectId(id)})
            return True
        except:
            return False
    
    def get_user(self, id):
        try:
            user = self.documento.find_one({"_id":ObjectId(id)})
            user['_id'] = JSONEncoder().encode(user['_id'])
            return user
        except:
            return False

    def update_user(self, id, user):
        try:
            usuario = self.documento.update_one({"_id":ObjectId(id)}, {"$set": user.getUser()})
            return usuario
        except pymongo.errors.CollectionInvalid as e: 
            print(e)
            return False

    def search_user(self, name, pag):
        page = (int(pag)-1)*3
        users = []
        regx = re.compile(name, re.IGNORECASE)
        try:
            cursor = self.documento.find({'nombre':regx}).skip(page).limit(3)
            for doc in cursor:
                doc['_id'] = JSONEncoder().encode(doc['_id'])
                users.append(doc)
            return users
        except:
            return False
