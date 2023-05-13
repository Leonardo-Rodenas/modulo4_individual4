def inicio():
    mensaje = """\nABP - Ejercicio Individual 4 - Continuación del trabajo. \n
    En base al diagrama de clases desarrollado en el ejercicio anterior, integra una estructura de herencia de
    tres niveles. Agregue un método por cada clase creada en su proyecto.\n
    Realice ejercicios para comprobar la herencia de métodos y atributos.\n
    Incorpore un ejemplo práctico de sobreescritura de métodos en su ejercicio individual.\n"""

    mensaje2 = """Herencia de tre niveles aplicada entre clase Persona - Reponedor - ReponedorExterno/ReponedorInterno\n
    Métodos sobreescritos: presentarse_a_trabajar (de clase Persona, sobreescrito en clase Reponedor) y externo_o_interno 
    (de clase reponedor, sobreescrito en los otros Repnedores)\n"""
    print(mensaje)
    print(mensaje2)
    return mensaje
