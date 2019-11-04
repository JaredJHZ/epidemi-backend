import json
from ..model.graphic import Graphic
from ..db.DB import Database


class GraphicService:

    def __init__(self):
        db = Database('epidemi')
        self.db = db.get_database()
        self.documento = self.db['casos']

    def get_data(self,datos):
        try:
            filtro = datos.get_graphic_info()
            cursor = self.documento.find({
                'enfermedad':filtro['enfermedad'],
                'year':int(filtro['year']),
                'mes':int(filtro['mes'])
            })
            datos = {
                "positivo":0,
                "negativo":0
            }
            for doc in cursor:
                if doc['resultado'] == "POSITIVO":
                    datos["positivo"] += 1
                else:
                    datos["negativo"] += 1

            return datos
        except:
            return False
       
