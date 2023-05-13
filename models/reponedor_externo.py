from .persona import Persona
from .reponedor import Reponedor

class ReponedorExterno(Reponedor, Persona):
    tipo_reponedor:str
    horario:int
    
    def __init__(self, nombre, apellido, rut, id_reponedor, edad, empresa, tipo_reponedor, horario):
        Persona.__init__(self, nombre, apellido, rut)
        Reponedor.__init__(self, nombre, apellido, rut, id_reponedor, edad, empresa)
        self.tipo_reponedor = tipo_reponedor
        self.horario = horario

    def externo_o_interno(self):
        super().lugar_a_reponer
        super().presentarse_a_trabajar()
        if self.tipo_reponedor == "Externo":
            print(f"{self.nombre} es un reponedor Externo que pertence a la empresa Te lo Vendo, su area de trabajo asignada según necesidad de la empresa es {Reponedor.lugar_a_reponer(self)}")
            print(f"{self.nombre} tiene un horario de trabajo de tipo: {self.horario}")
        else:
            print("El tipo de reponedor no es valido")
