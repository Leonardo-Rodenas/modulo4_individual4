from .persona import Persona
from .reponedor import Reponedor

class ReponedorInterno(Reponedor, Persona):
    tipo_reponedor:str
    area_asignada:str
    
    def __init__(self, nombre, apellido, rut, id_reponedor, edad, empresa, tipo_reponedor, area_asignada):
        Persona.__init__(self, nombre, apellido, rut)
        Reponedor.__init__(self, nombre, apellido, rut, id_reponedor, edad, empresa)
        self.tipo_reponedor = tipo_reponedor
        self.area_asignada = area_asignada

    def externo_o_interno(self):
        super().presentarse_a_trabajar()
        if self.tipo_reponedor == "Interno":
            print(f"{self.nombre} es un reponedor Interno que pertence a la empresa Te lo Vendo, su area asignada de trabajo es {self.area_asignada}")
        else:
            print("El tipo de reponedor no es valido")

    

