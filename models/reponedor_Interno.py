from persona import Persona
from reponedor import Reponedor

class ReponedorInterno(Reponedor, Persona):
    tipo_reponedor:str = "Interno"
    area_asignada:str
    
    def __init__(self, nombre, apellido, rut, id_reponedor, edad, empresa, tipo_reponedor, area_asignada):
        Persona.__init__(self, nombre, apellido, rut)
        Reponedor.__init__(self, id_reponedor, edad, empresa)
        self.tipo_reponedor = tipo_reponedor
        self.area_asignada = area_asignada

    def externo_o_interno(self, tipo):
        super().presentarse_a_trabajar()
        tipo = "Interno"
        if tipo == "Interno":
            print(f"{self.nombre} es un reponedor Interno que pertence a la empresa Te lo Vendo, su area asignada de trabajo es {self.area_asignada}")
        else:
            print("El tipo de reponedor no es valido")

    
# reponedorInterno = ReponedorInterno("Juan", "Perez", "12.456.123-k", "1234567890", 30,"Te lo Vendo", "Interno", "area")
# reponedorInterno.externo_o_interno("Interno")

