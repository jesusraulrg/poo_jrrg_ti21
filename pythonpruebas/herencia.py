"""
  herencia.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: FEBRERO 2023
  Descripción: Declaración de una clase y metodos a partir de otra clase heredada
"""

class Persona: #Declaración de la clase PERSONA

    __nombre = None #Creación de una variable privada, tomando el valor de NONE por defecto
    __edad = None #Creación de una variable privada, tomando el valor de NONE por defecto

    def __init__(self): #Función que crea un método
        print("Persona") #Imprime Persona en pantalla como nombre de la clase
    def setNombre(self,nombre): #Se determina un método de la clase Persona
        self.__nombre = nombre #La variable nombre se vuelve privada

class Alumno(Persona): #Declaración de la clase Alumno, heredando los metodos de Persona

    __matricula = None #Creación de una variable privada, tomando el valor de NONE por defecto
    __nombre = None #Creación de una variable privada, tomando el valor de NONE por defecto
    
    def __init__(self): #Función que crea un método
        super().__init__() #Llama al constructor de la clase Persona
        print ("Alumno") #Imprime Alumno en pantalla

objeto_persona = Persona() #Se crea el objeto Persona
objeto_alumno = Alumno() #Se crea el objeto Alumno

print(dir(objeto_persona)) #Imprime el directorio del objeto persona
print(dir(objeto_alumno)) #Imprime el directorio del objeto alumno