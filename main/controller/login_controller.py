from flask_restful import Resource
from flask import request
from ..service.login_service import LoginService


def get_user_info(req):
    info = req.get_json(force=True)
    email = info['email']
    password = info['password']
    return {
        'email':email,
        'password':password
    }

class LoginController(Resource):

    def post(self):
        user_info = get_user_info(request)
        user_auth = LoginService.login(user_info['email'],user_info['password'])
        if user_auth[0]:
            return {
                "mensaje":user_auth[1],
                "token":user_auth[2],
                "permiso":user_auth[3]
            }, 201
        else:
            return {
                "mensaje": user_auth[1]
            }, 401

    def get(self):
        return {
            "mensaje":"favor de registrarse"
        }
    
    def options(self):
        pass