from models.persona import Persona
import random 

class Vendedor(Persona):
    nombre:str
    apellido:str
    seccion:str
    cargo:str
    edad:int
    clientes:list
    productos = {}

    def __init__(self, nombre, apellido, rut, seccion, cargo="Vendedor", edad=None, clientes=[]):
        super().__init__(nombre, apellido, rut)
        self.seccion = seccion
        self.cargo = cargo
        self.edad = edad
        self.clientes = clientes

    def registrar_cliente(self, nombre, apellido, correo_cliente, telefono_cliente:int, *edad_cliente:int):
        nuevo_cliente = {"nombre": nombre, "apellido": apellido, "correo": correo_cliente, "telefono": telefono_cliente, "edad": edad_cliente}
        self.clientes.append(nuevo_cliente)
        print(f"Nuevo cliente: {nombre} {apellido} registrado con éxito")

    def vender(self, nombre, apellido, producto, precio):
        venta = {"producto": producto, "precio": precio}
        for cliente in self.clientes:
            if cliente["nombre"] == nombre and cliente["apellido"] == apellido:
                if "ventas" not in cliente:
                    cliente["ventas"] = []
                cliente["ventas"].append(venta)
                print(f"¡Venta realizada! {nombre} ha comprado {producto} por ${precio}.")
                return
        print(f"No se encontró al cliente {nombre} {apellido} en la lista de clientes.")

    def controlar_stock(self, producto, cantidad):
        if producto not in self.productos:
            self.productos[producto] = cantidad
        else:
            self.productos[producto] += cantidad
        print(f"El stock de {producto} es ahora de {self.productos[producto]}.")

    def hacer_oferta(self, producto, precio):
        descuento = round(random.uniform(0.05, 0.1) * precio)
        precio_descuento = round(precio - descuento, 2)
        print(f"¡Oferta especial para {producto}! Precio original: ${precio}. Descuento: ${descuento}. Precio con descuento: ${precio_descuento}.")
