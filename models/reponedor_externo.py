from persona import Persona
from reponedor import Reponedor

class ReponedorExterno(Reponedor, Persona):
    tipo_reponedor:str = "Externo"
    horario:int
    
    def __init__(self, nombre, apellido, rut, id_reponedor, edad, empresa, tipo_reponedor, horario):
        Persona.__init__(self, nombre, apellido, rut)
        Reponedor.__init__(self, id_reponedor, edad, empresa)
        self.tipo_reponedor = tipo_reponedor
        self.horario = horario

    def externo_o_interno(self, tipo):
        super().presentarse_a_trabajar()
        tipo = "Externo"
        if tipo == "Externo":
            print(f"{self.nombre} es un reponedor Externo que pertence a la empresa Te lo Vendo, su area de trabajo asignada es según necesidad de la empresa al momento de prersentarse a trabajar")
        else:
            print("El tipo de reponedor no es valido")
