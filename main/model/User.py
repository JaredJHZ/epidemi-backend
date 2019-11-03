from ..tools.security import Security

class User:

    def __init__(self, nombre = None, puesto = None, permiso = None, email = None ,password = None):
        self.nombre = nombre
        self.puesto = puesto
        self.permiso = permiso
        self.email = email
        self.password = Security.generate_password(password)

    def getUser(self):
        return {
            'nombre': self.nombre, 
            'puesto': self.puesto, 
            'permiso': self.permiso,
            'email': self.email,
            'password':self.password
            }
