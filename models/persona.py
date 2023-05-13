class Persona:
    nombre:str
    apellido:str
    rut:str

    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut 

    def presentarse_a_trabajar(self):
        print(f"{self.nombre} {self.apellido} se está presentando a trabajar en la empresa.")