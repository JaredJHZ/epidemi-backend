class Case:

    def __init__(self, expediente, enfermedad, mes, year, resultado, nombre_paciente):
        self.expediente = expediente
        self.enfermedad = enfermedad
        self.mes = mes
        self.year = year
        self.resultado = resultado
        self.nombre_paciente = nombre_paciente

    def get_case_info(self):
        return {
            "numero_expediente": self.expediente,
            "enfermedad": self.enfermedad,
            "mes": self.mes,
            "year": self.year,
            "resultado": self.resultado,
            "nombre_paciente":self.nombre_paciente
        }