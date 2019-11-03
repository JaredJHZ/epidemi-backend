from flask_restful import Resource
from flask import request

from ..service.user_service import UserService
from ..tools.json_encoder import JSONEncoder
from ..tools.security import Security
from ..model.User import User


user_service = UserService()

def create_user_object(req):
    info = req.get_json(force=True)
    nombre = info['nombre']
    puesto = info['puesto']
    permiso = info['permiso']
    email = info['email']
    password = info['password']
    
    return User(nombre, puesto, permiso, email ,password)

class UserController(Resource):
    def get(self):
        return {
            'users': user_service.get_all_users_count()
        }, 201
    
    def post(self):
        token = request.headers.get("Authorization")
        print(token);
        if Security.verifyToken(token):
            usuario = create_user_object(request)
            if user_service.save_user(usuario):
                return {
                    "mensaje":"usuario creado"
                }, 201
            else:
                return {
                    "mensaje": "ERROR usuario no creado"
                }, 405
        else:
            return {
                "mensaje":"Error en autenticacion"
            }, 401

    def options(self):
        pass

class UserPagination(Resource):
    def get(self,pag):
        user = user_service.get_users_pagination(pag)
        if user:
            return {
                "usuario":user
            }, 201
        else:
            return {
                "mensaje":"No se encontraron los usuarios"
            }, 401
    
    def options(self,pag):
        pass

class UserControllerParameter(Resource):
    def get(self, id):
        user = user_service.get_user(id) 
        if user :
            return {
                "usuario":user
            }, 201
        else:
            return {
                "mensaje": "No se encontró el usuario"
            }, 401
    
    def delete(self,id):
        if user_service.delete_user(id):
            return {
                "mensaje": "El usuario ha sido eliminado"
            }
        else:
            return {
                "mensaje":"El usuario no se econtró"
            }

    def put(self,id):
        usuario = create_user_object(request)
        if user_service.update_user(id, usuario):
            return {
                "mensaje":"usuario editado correctamente"
            }, 201
        else:
            return {
                "mensaje": "No se encontró el usuario"
            }, 401

    def options(self,id):
        pass
