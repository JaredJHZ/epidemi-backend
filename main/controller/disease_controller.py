from flask_restful import Resource
from flask import request

from ..model.Disease import Disease
from ..service.disease_service import DiseaseService
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder


disease_service = DiseaseService()

def create_disease_object(req):
    info = req.get_json(force= True)
    nombre_enfermedad = info['nombre_enfermedad']

    return Disease(nombre_enfermedad)

class DiseaseController(Resource):

    def get(self):
        try:
            return {
                "diseases":disease_service.get_all_diseases_count()
            }, 201
        except:
            return {
                'mensaje':'error en el servidor'
            }, 501

    def post(self):
        disease = create_disease_object(request)
        if disease_service.save_disease(disease):
            return {
                "mensaje":"enfermedad creada"
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501

    def options(self):
        pass

class DiseasesPaginationController(Resource):
    def get(self,pag):
        diseases = disease_service.get_diseases_pagination(pag)
        if diseases:
            return {
                "enfermedades":diseases
            }, 201
        else:
            return {
                "mensaje":"No se encontraron las enfermedades"
            }, 401
    
    def options(self,pag):
        pass

class DiseasesParameterController(Resource):

    def get(self,id):
        disease = disease_service.get_disease(id)
        if disease:
           return {
               "enfermedad":disease
           }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501

    def delete(self,id):
        if disease_service.delete_disease(id):
            return {
                "mensaje": "enfermedad eliminado"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
       
    def put(self,id):
        disease = create_disease_object(request)
        if disease_service.update_disease(id,disease):
            return {
                "mensaje":"datos de la enfermedad actualizados"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
    
    def options(self,id):
        pass

class AllDiseasesController(Resource):

    def get(self):
        diseases = disease_service.get_all_diseases()
        if diseases:
            return {
                "diseases":diseases
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }
    
    def options(self):
        pass

class SearchDiseaseController(Resource):

    def post(self,pag):
        info = request.get_json(force= True)
        nombre_enfermedad = info['nombre_enfermedad']
        diseases = disease_service.search_disease(nombre_enfermedad,pag)
        if diseases:
            return {
                "diseases": diseases
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 404
    def options(self):
        pass
