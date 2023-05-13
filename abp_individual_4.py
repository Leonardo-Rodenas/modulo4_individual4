from models.persona import Persona
from models.cliente import Cliente
from models.vendedor import Vendedor
from models.proveedor import Proveedor
from models.repartidor import Repartidor
from models.reponedor import Reponedor

#instancias de clase persona
persona1 = Persona("Bernardo", "Cortez", "17.236.459-8")
persona1.presentarse_a_trabajar()

# Instancias y prueba de métodos para la clase cliente
cliente1 = Cliente(nombre="Juan", apellido="Soto", rut="12345678-9")
cliente1.actualizar_datos("Juan")
print()
cliente1.solicitar_tarjeta()
print()
cliente1.comprar("Ipad Pro", 1, "menos5%")
print()
cliente1.solicitar_entrega()

# Instancias y prueba de métodos para la clase vendedor
vendedor1 = Vendedor("Juan", "Pérez", "17.236.459-8", "Electrónica")
vendedor2 = Vendedor("Pedrito", "Pascal", "14.259.147-5", "Línea Blanca", "Gerente", 48)
vendedor1.registrar_cliente("Roberto", "Sepúlveda", "correofalso123@gmail.com", 123465789, 34)
vendedor2.registrar_cliente("Leandro", "Merino", "correofalso465@gmail.com", 147258369, 33)
print()
vendedor1.vender("Roberto", "Sepúlveda", "Notebook Gamer", 650000)
vendedor2.vender("Leandro", "Merino", "Playstation 5", 700000)
print()
vendedor1.controlar_stock("Notebook Gamer", 10)
vendedor2.controlar_stock("Playstation 5", 4)
print()
vendedor1.hacer_oferta("Notebook Gamer", 650000)
vendedor2.hacer_oferta("Playstation 5", 700000)
print()

# Instancias y prueba de métodos para la clase proveedor
proveedor1 = Proveedor("76.256.128-K", "Mademsa", "Lavadoras", 22) # Atributo opcional = cargo
proveedor2 = Proveedor("10.256.478.3", "Dell", "Computadores", 35, "Gerente")
proveedor1.validar_nombre_empresa("Mademsa") # EMPRESA VALIDA
proveedor2.validar_nombre_empresa("HP") # EMPRESA NO VALIDA
print()
proveedor1.validar_cantidad_de_productos(10) # CANTIDAD VALIDA
proveedor2.validar_cantidad_de_productos(40) # CANTIDAD INVALIDA
print()
proveedor1.validar_rut_regex("14.256.128-K") # RUT VALIDO
proveedor2.validar_rut_regex("17.456.147-A") # RUT NO VALIDO
print()
proveedor1.solicitar_firma_documentos("Mademsa") # Todo correcto, responder "s"
proveedor2.solicitar_firma_documentos("HP", "Carlos Toro") # No firmar, Carlos Toro no es el proveedor2, es María González
print()

# Instancias y prueba de métodos para la clase repartidor
repartidor1 = Repartidor("Leela", 123456789, "Marge", 5,12345678, "Avenida Siempreviva #742, Springfield") # Instancia repartidor sin apellido (opcional)
repartidor2 = Repartidor("Fry", 1234561324, "Bart", 6, "12345678") # Instancia repartidor sin dirección de envío y apellido (opcionales)
repartidor1.tomar_pedido("Leela", "Homero", "Hamburguesas Krusty #36, Springfield")
repartidor2.tomar_pedido("Fry")
print
repartidor1.validar_telefono() # Salida: Validación telefónica - OK
repartidor2.validar_telefono() # Salida: Validación teléfonica - ERROR
print()
repartidor1.validar_cantidad_productos(5, 10)
repartidor2.validar_cantidad_productos(20, 10)
print()
repartidor1.entregar_pedido()
repartidor2.entregar_pedido()

# Instancias y prueba de métodos para la clase reponedor
reponedor1 = Reponedor("Guillermo", "Perez", "18.456.789-3", "id_repo01", 25, "Te lo Vendo")
reponedor2 = Reponedor("Mateo", "Castillo", "15.789.456-5", "id_repo02", 36, "Te lo Vendo")
reponedor1.presentarse_a_trabajar()
reponedor2.presentarse_a_trabajar()
