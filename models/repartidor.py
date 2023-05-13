from models.persona import Persona

class Repartidor (Persona):
    nombre:str 
    apellido:str
    telefono:int
    nombre:str
    num_pedidos:int 
    telefono_cliente:int
    direccion_envio:str 

    def __init__(self,  telefono, nombre, rut, num_pedidos, telefono_cliente, direccion_envio=None, apellido=None):
        super().__init__(nombre, apellido, rut)
        self.apellido = apellido
        self.telefono = telefono
        self.nombre = nombre
        self.num_pedidos = num_pedidos
        self.telefono_cliente = telefono_cliente
        self.direccion_envio = direccion_envio

    def tomar_pedido(self, nombre, *args):
        self.nombre = nombre
        if len(args) == 1:
            self.nombre = args[0]
        if len(args) == 2:
            self.nombre = args[0]
            self.direccion_envio = args[1]
        if len(args) == 3:
            self.nombre = args[0]
            self.direccion_envio = args[1]
            self.telefono_cliente = args[2]
        self.num_pedidos += 1
        print(f"El repartidor {self.nombre} tiene {self.num_pedidos} pedidos asignados")
        print(f"{self.nombre} ha tomado un pedido para cliente: {self.nombre} (fono: {self.telefono_cliente}), entregar en dirección: {self.direccion_envio}. \n")

    def validar_telefono(self):
        telefono = type(self.telefono_cliente)
        if telefono == int:
            print(self.nombre + " ha verificado el teléfono del cliente. Resultado: Verificación teléfonica - OK")
            return True
        else:
            print(self.nombre + " ha verificado el teléfono del cliente. Resultado: Verificación teléfonica - ERROR")
            return False
    
    def validar_cantidad_productos(self, productos, cantidad_maxima):
        if productos <= cantidad_maxima:
            print("Cantidad de productos permitida, Repartidor: " + self.nombre + " es posible cargar y enviar a destino")
            return True
        else:
            print("Cantidad de productos no permitida, Repartidor: "+ self.nombre + " no es posible cargar y enviar a destino")
            return False
    
    def entregar_pedido(self):
        if self.num_pedidos == 0:
            print("No hay pedidos para entregar.")
            return
        if self.direccion_envio is None:
            print("El pedido del repartidor " + self.nombre + " aún no está listo para la entrega. Falta la dirección de envío.")
            return
        self.pedido_entregado = True
        self.num_pedidos -= 1
        print("El pedido del repartidor " + self.nombre + " se ha entregado con éxito.")
