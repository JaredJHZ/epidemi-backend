from flask_restful import Resource
from flask import request

from ..model.Case import Case
from ..service.case_service import CaseService
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder

case_service = CaseService()

def create_case_object(req):
    info = req.get_json(force= True)
    paciente = info['paciente']
    enfermedad = info['enfermedad']
    mes = info['mes']
    year = info['year']
    resultado = info['resultado']
    return Case(paciente, enfermedad, mes, year, resultado)

class CaseController(Resource):

    def get(self):
        try:
            return {
                "cases":case_service.get_all_cases_count()
            }, 201
        except:
            return {
                'mensaje':'error en el servidor'
            }, 501
    
    def post(self):
        case = create_case_object(request)
        if case_service.save_case(case):
            return {
                "mensaje":"caso creado"
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501
    
    def options(self):
        pass

class CasesPaginationController(Resource):
    def get(self,pag):
        cases = case_service.get_cases_pagination(pag)
        if cases:
            return {
                "cases":cases
            }, 201
        else:
            return {
                "mensaje":"No se encontraron los casos"
            }, 401
    
    def options(self,pag):
        pass

class CasesParameterController(Resource):

    def get(self,id):
        case = case_service.get_case(id)
        if case:
           return {
               "case":case
           }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501

    def delete(self,id):
        if case_service.delete_case(id):
            return {
                "mensaje": "caso eliminado"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
       
    def put(self,id):
        case = create_case_object(request)
        if case_service.update_case(id,case):
            return {
                "mensaje":"datos del caso actualizados"
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }, 501
    
    def options(self,id):
        pass

class AllCasesController(Resource):

    def get(self):
        cases = case_service.get_all_cases()
        if cases:
            return {
                "cases":cases
            }, 201
        else:
            return {
                "mensaje":"error en el servidor"
            }
    
    def options(self):
        pass