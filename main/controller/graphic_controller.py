from flask_restful import Resource
from flask import request

from ..model.graphic import Graphic
from ..service.graphic_service import GraphicService
from ..db.DB import Database
from ..tools.json_encoder import JSONEncoder

graphic_server = GraphicService()

def create_graphic_object(req):
    info = req.get_json(force= True)
    month = info['month']
    year = info['year']
    disease = info['disease']

    return Graphic(month,year, disease)

class GraphicController(Resource):

    def post(self):
        data = create_graphic_object(request)
        datos = graphic_server.get_data(data)
        if datos:
            return {
                "datos":datos
            }, 201
        else:
            return {
                "mensaje": "error en el servidor"
            }, 501

    def options(self):
        pass