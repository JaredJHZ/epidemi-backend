class Disease:

    def __init__(self,nombre_enfermedad):
        self.nombre_enfermedad = nombre_enfermedad

    def get_disease_info(self):
        return {
            "nombre_enfermedad":self.nombre_enfermedad
        }