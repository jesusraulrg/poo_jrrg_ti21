"""
  alumno.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 17 DE FEBRERO DE 2023
  Descripción: Declaración de una clase y metodos a partir de otra clase herdada desde un archivo distinto
"""

from persona import Persona #Importa del archivo persona.py la clase Persona

class Alumno(Persona): #Crea la clase Alumno y hereda de la clase Persona

    def __init__(self) -> None: #Constructor de la clase Alumno
        super().__init__() #Llama al constructor de la clase Persona
        print("Constructor Alumno") #Muestra el mensaje "Constructor Alumno"

objeto_alumno = Alumno() #Crea un objeto de la clase Alumno e invoca al contructor
objeto_alumno.setNombre("Jesus") #Llama al metodo setNombre de la clase Persona y le pasa el parametro "Jesus"
print(objeto_alumno.getNombre()) #Llama al metodo getNombre e imprime el valor del nombre