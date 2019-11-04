class Graphic:

    def __init__(self, month, year, disease):
        self.month = month
        self.year = year
        self.disease = disease

    def get_graphic_info(self):
        return {
            "mes":self.month,
            "year":self.year,
            "enfermedad":self.disease
        }
