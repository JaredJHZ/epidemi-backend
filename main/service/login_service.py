import json
from bson import ObjectId
import pymongo

from ..model.User import User
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder 
from ..tools.security import Security

class LoginService:

    @staticmethod
    def login(mail,password):
        databaseInstance = Database('epidemi')
        db = databaseInstance.get_database()
        documento = db["usuarios"]
        user = documento.find_one({'email':mail})

        if user and "password" in user:
            password_in_db = user['password']
            permiso = user['permiso']
            if Security.check_password(password_in_db, password):
                token = Security.generate_token(user)
                token = token[2:-1]
                return (True, "sesion iniciada",token, permiso)
            else:
                return (False, "error en la contraseña" )
        else:
            return (False, "error usuario no registrado")
        