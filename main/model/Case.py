class Case:

    def __init__(self, paciente, enfermedad, mes, year, resultado):
        self.paciente = paciente
        self.enfermedad = enfermedad
        self.mes = mes
        self.year = year
        self.resultado = resultado

    def get_case_info(self):
        return {
            "paciente": self.paciente,
            "enfermedad": self.enfermedad,
            "mes": self.mes,
            "year": self.year,
            "resultado": self.resultado
        }