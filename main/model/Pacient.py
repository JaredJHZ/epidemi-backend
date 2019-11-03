class Pacient:

    def __init__(
        self,apellido_paterno, apellido_materno, 
        nombre, edad, tipo_sangre, calle, 
        numero ,colonia, ciudad, localidad, sexo,
        fecha_nacimiento, peso, numero_expediente
        ):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.calle = calle
        self.numero = numero
        self.colonia = colonia
        self.ciudad = ciudad
        self.localidad = localidad
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso,
        self.numero_expediente = numero_expediente
    
    def get_pacient_info(self):
        return {
            "nombre":self.nombre,
            "apellido_paterno":self.apellido_paterno,
            "apellido_materno":self.apellido_materno,
            "edad":self.edad,
            "tipo_sangre":self.tipo_sangre,
            "calle":self.calle,
            "numero":self.numero,
            "colonia":self.colonia,
            "ciudad":self.ciudad,
            "localidad":self.localidad,
            "sexo":self.sexo,
            "fecha_nacimiento":self.fecha_nacimiento,
            "peso":self.peso,
            "numero_expediente": self.numero_expediente
        }

