from models.persona import Persona

class Cliente(Persona):
    nombre:str
    apellido:str
    rut_cliente:str
    telefono_cliente:int 
    compras:list = []
    cupon_descuento:str
    edad_cliente:int
    correo_cliente:str
    tiene_tarjeta:bool = False
        
    def __init__(self, nombre, apellido, rut, **kwargs):
        super().__init__(nombre, apellido, rut)
        if "rut" in kwargs:
            self.rut_cliente = kwargs["rut"]
        if "correo" in kwargs:
            self.correo_cliente = kwargs["correo"]
        if "telefono" in kwargs:
            self.telefono_cliente = kwargs["telefono"]
        if "edad" in kwargs:
            self.edad_cliente = kwargs["edad"]
        if "compra" in kwargs:
            self.compras = kwargs["compra"]
        if "cupon" in kwargs:
            self.cupon_descuento = kwargs["cupon"]

    def actualizar_datos(self, nombre):
        while True: 
            print(f"Bienvenido {nombre}, Qué datos desea actualizar?")
            print("Nombre - Escribe n\nApellido - Escribe a\nRut - Escribe r\nCorreo - Escribe c\nTeléfono - Escribe t\nEdad - Escribe e\nSalir - Escribe s\n")
            opcion = input("Escribe la letra correspondiente al dato a actualizar: ")
            if opcion.lower() != "s":
                if opcion.lower() == "n":
                    self.nombre = input("Ingrese el nuevo nombre: ")
                elif opcion.lower() == "a":
                    self.apellido = input("Ingrese el nuevo apellido: ")
                elif opcion.lower() == "r":
                    self.rut_cliente = input("Ingrese el nuevo RUT: ")
                elif opcion.lower() == "c":
                    self.correo_cliente = input("Ingrese el nuevo correo electrónico: ")
                elif opcion.lower() == "t":
                    self.telefono_cliente = int(input("Ingrese el nuevo número de teléfono: "))
                elif opcion.lower() == "e":
                    self.edad_cliente = int(input("Ingrese la nueva edad: "))
                else:
                    print("Opción inválida")
                    break
            elif opcion.lower() == "s":
                break
        print("Datos actualizados")

    def solicitar_tarjeta(self):

        if self.tiene_tarjeta:
            print("Ya tienes una tarjeta")
            return 
        direccion = input("Ingresa tu dirección para enviar la tarjeta: ")
        while not direccion:
            direccion = input("Por favor, ingresa una dirección válida: ")
        identificacion = input("Ingresa tu número de identificación (ej. RUT): ")
        while not identificacion:
            identificacion = input("Por favor, ingresa un número de identificación válido: ")
        print("Procesando solicitud de tarjeta para el cliente", self.nombre, self.apellido, "con identificación", identificacion)
        print("La tarjeta será enviada a la dirección", direccion)
        self.tiene_tarjeta = True
    
    def comprar(self, producto, cantidad, cupon_descuento=None):
        if cupon_descuento == "menos5%":
            descuento = 0.05  # ejemplo: 5% de descuento
            precio_unitario = 72500  # ejemplo: precio sin descuento
            precio_descuento = int(precio_unitario * (1 - descuento))
            precio_total = cantidad * precio_descuento
            print(f"¡Cupón de descuento aplicado por {self.nombre}! Precio total con descuento: ${precio_total}")
        else:
            precio_unitario = 72500  
            precio_total = int(cantidad * precio_unitario)
            compra = {"producto": producto, "cantidad": cantidad, "precio_unitario": precio_unitario, "precio_total": precio_total}
            print(f"Compra realizada por {self.nombre}! Precio total: ${precio_total}")
            self.compras.append(compra)

    def solicitar_entrega(self):
        print(f"Bienvenido {self.nombre}, ¿desea entrega en tienda o despacho?")
        opcion = input("Ingrese T para entrega en tienda o D para despacho: ").lower()
        
        while opcion not in ["t", "d"]:
            opcion = input("Ingrese una opción válida (T o D): ").lower()
            
        if opcion == "t":
            print("La entrega se realizará en tienda")
        else:
            direccion = input("Ingresa la dirección de entrega: ")
            telefono = input("Ingresa el número de teléfono para contacto: ")    
            print(f"La entrega se realizará en la dirección {direccion} y el teléfono de contacto es {telefono}")
