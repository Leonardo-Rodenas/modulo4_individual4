import re

class Proveedor:
    nombre:str
    rut_proveedor: str
    empresa:str
    producto_provisto:str
    cantidad_provista:int
    cargo:str

    def __init__(self, rut_proveedor, empresa, producto_provisto, cantidad_provista, cargo="Proveedor"):
        self.rut_proveedor = rut_proveedor
        self.empresa = empresa
        self.producto_provisto = producto_provisto
        self.cantidad_provista = cantidad_provista
        self.cargo = cargo

    def validar_nombre_empresa(self, nombre_empresa):
        if nombre_empresa == self.empresa:
            print(f"El nombre de la empresa en la factura ({nombre_empresa}), coincide con la empresa donde se está entregando ({self.empresa}).")
            return True
        else:
            print(f"El nombre de la empresa en la factura ({nombre_empresa}), NO coincide con la empresa donde se está entregando ({self.empresa}).")
            return False
    
    def validar_cantidad_de_productos(self, cantidad_entregada):
        if cantidad_entregada <= self.cantidad_provista:
            print(f"La cantidad de productos a provistos a entregar ({self.cantidad_provista}) comparada con la cantidad entregada ({cantidad_entregada}) es válida.")
            return True
        else:
            print(f"La cantidad de productos a provistos a entregar ({self.cantidad_provista}) comparada con la cantidad entregada ({cantidad_entregada}) NO es válida.")
            return False  

    def validar_rut_regex(self, rut):
        patron = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$')  #   14.256.128-K
        if not patron.match(rut):
            print(f"El rut {rut} es incorrecto")
            return False
        rut = rut.replace(".", "").replace("-", "").upper() #       14256128K
        dv = rut[-1] # K
        rut = rut[:-1] # 14256128  
        suma = 0
        multiplicador = 2
        for i in reversed(range(len(rut))): # 82165241
            suma += int(rut[i]) * multiplicador
            multiplicador += 1 
            if multiplicador > 7:
                multiplicador = 2 # (8*2)+(2*3)+(1*4)+(6*5)+(5*6)+(2*7)+(4*2)+(1*3) = 16 + 6 + 4 +30 +30 +14 +8 + 3 = 111/11 = 10.09 (entero 10, resto=0.9 +- 1)
        verificador = 11 - (suma % 11) # 11- 1 = 10
        if verificador == 11:
            verificador = "0"
            print(f"El rut {rut} es correcto")
        elif verificador == 10:
            verificador = "K"
            print(f"El rut {rut} es correcto")
        else:
            verificador = str(verificador)
            print(f"El rut {rut} es correcto")
        return verificador == dv

    def solicitar_firma_documentos(self, nombre_empresa, *args):
        if len(args) == 1:
            self.nombre = args[0]
        if len(args) == 2:
            self.nombre = args[0]
            self.cantidad_provista = args[1]
        if len(args) == 3:
            self.nombre = args[0]
            self.cantidad_provista = args[1]
            self.rut_proveedor = args[2]
        print(f"Por favor, representante de la empresa {nombre_empresa}, valide los datos y firme para confirmar la entrega de productos.")
        print("Nombre proveedor: " + self.empresa)
        print("Cantidad Provista entrega: " + str(self.cantidad_provista))
        print("Rut Proveedor" + self.rut_proveedor)
        respuesta = input("¿Desea firmar los documentos? (s/n): ")
        if respuesta == "s":
            print("Datos validados. Documentos firmados correctamente.\n")
        else:
            print("Datos no válidos. No se ha firmado la documentación.\n")
