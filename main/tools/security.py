import jwt
import json
from werkzeug.security import generate_password_hash, check_password_hash

secret = "jared123"

class Security:

    @staticmethod
    def generate_password(password):
        try:
            hashed_password = generate_password_hash(password)
            return hashed_password
        except:
            return False
    
    @staticmethod
    def check_password(password_in_db, password_typed):
        return check_password_hash(password_in_db, password_typed )

    @staticmethod
    def generate_token(user):
        usuario = {
            "nombre":user['nombre'],
            "permiso":user['permiso'],
            "email":user['email']
        }
    
        token = jwt.encode(usuario,"secret")
        return str(token)

    @staticmethod
    def verifyToken(token):
        try:
            info = jwt.decode(token,"secret")
            print(info)
            return info
        except jwt.ExpiredSignature:
            return False

