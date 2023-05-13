import random
from persona import Persona

class Reponedor(Persona):
    id_reponedor:str
    edad:int
    empresa:str

    def __init__(self,nombre,apellido, rut, id_reponedor, edad, empresa):
        super().__init__(nombre, apellido, rut)
        self.id_reponedor = id_reponedor
        self.edad = edad
        self.empresa = empresa 

    def lugar_a_reponer(self):
        lugares = ["bodega", "sala de ventas", "vitrinas", "sección 1", "sección 2", "sección 3"]
        return random.choice(lugares)

    def presentarse_a_trabajar(self):
        super().presentarse_a_trabajar()
        print(f"{self.nombre} (Id_reponedor: {self.id_reponedor}) está revisando su lista de tareas antes de comenzar a reponer en {self.lugar_a_reponer()}.")

    def externo_o_interno(self):
        pass    

