import json
import pymongo
from flask_restful import Resource
from flask import request
from bson import ObjectId
from ..model.Pacient import Pacient
from ..service.pacient_service import PacientService
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder 

pacient_service = PacientService()

def create_pacients_object(req):
    info = req.get_json(force=True)
    nombre = info['nombre']
    apellido_paterno = info['apellido_paterno']
    apellido_materno = info['apellido_materno']
    edad = info['edad']
    tipo_sangre = info['tipo_sangre']
    calle = info['calle']
    numero = info['numero']
    colonia = info['colonia']
    ciudad = info['ciudad']
    localidad = info['localidad']
    sexo = info['sexo']
    fecha_nacimiento = info['fecha_nacimiento']
    peso = info['peso']
    numero_expediente = info['numero_expediente']


    return Pacient(apellido_paterno, apellido_materno, 
                    nombre , edad, tipo_sangre,
                    calle, numero, colonia, ciudad, localidad, 
                    sexo, fecha_nacimiento, peso, numero_expediente)

class PacientController(Resource):
    def get(self):
        try:
            return {
            "pacients": pacient_service.get_all_pacients_count()
            }, 201
        except:
            return {
                "mensaje": "error en el servidor"
            }, 501
    
    def post(self):
        pacient = create_pacients_object(request)
        if pacient_service.save_pacient(pacient):
            return {
                "mensaje": "paciente creado"
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501
    
    def options(self):
        pass

class PacientsPagination(Resource):
    def get(self,pag):
        pacients = pacient_service.get_pacients_pagination(pag)
        if pacients:
            return {
                "pacients":pacients
            }, 201
        else:
            return {
                "mensaje":"No se encontraron los pacientes"
            }, 401
    
    def options(self,pag):
        pass

class PacientParameterController(Resource):

    def get(self,id):
        pacient = pacient_service.get_pacient(id)
        if pacient:
           return {
               "pacient":pacient
           }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501

    def delete(self,id):
        if pacient_service.delete_pacient(id):
            return {
                "mensaje": "paciente eliminado"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
       
    def put(self,id):
        pacient = create_pacients_object(request)
        if pacient_service.update_pacient(id, pacient):
            return {
                "mensaje":"datos del paciente actualizados"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
    
    def options(self,id):
        pass

class AllPacientsController(Resource):

    def get(self):
        pacients = pacient_service.get_all_pacients()
        if pacients:
            return {
                "pacients":pacients
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }
    
    def options(self):
        pass

class SearchPacientController(Resource):

    def post(self,pag):
        info = request.get_json(force= True)
        nombre = info['nombre_paciente']
        print(nombre)
        pacients = pacient_service.search_pacient(nombre,pag)
        if pacients:
            return {
                "pacients": pacients
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 404
    def options(self):
        pass