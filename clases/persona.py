"""
  persona.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 17 DE FEBRERO DE 2023
  Descripción: Declaración de una clase y metodos
"""

class Persona: #Clase Persona

    __nombre = None

    def __init__(self) -> None: #Constructor de la clase Persona
        print("Constructor Persona") #Imprime el texto "Constructor Persona"

    def setNombre(self, nombre:str)->None: #Metodo para modificar el valor de la variable
        self.__nombre = nombre #Asigna el valor de la variable privada __nombre

    def getNombre(self)->str: #Metodo para regresar el vaor de la varible privada __nombre
        return self.__nombre #Regresa el valor de la varible privada __nombre