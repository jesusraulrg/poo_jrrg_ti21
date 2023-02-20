"""
  persona.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: FEBRERO 2023
  Descripción: Declaración de una clase y objetos
"""

class Persona: #Se crea la clase Persona 

    __nombre = None #la variable privada nombre toma el valor de None por defecto
    __email = None #la variable privada email toma el valor de None por defecto

    def __init__ (self): #Función que crea un método
        print("Persona") #Imprime Persona en pantalla
    
    def setNombre (self,nombre): #Se determina un método de la clase Persona
        self.__nombre = nombre #La variable nombre se vuelve privada
    def getNombre(self): #La función solicita a la variable
        return self.__nombre #Regresa el resultado de la variable como metodo de una clase
    
    def __init__(self): #Función que crea un método
        print("Email") #Imprime Persona en pantalla
    
    def setEmail (self,email): #Se determina un método de la clase Persona
        self.__email = email #La variable email se vuelve privada
    def getEmail(self): #La función solicita a la variable
        return self.__email #Regresa el resultado de la variable como metodo de una clase

dejah = Persona() #Se asigna valor a la clase 
dejah.setNombre("Dejah") #Se agrega un valor al metodo Nombre
dejah.setEmail("dejah@hotmail.com") #Se agrega un valor al métodoEmail
print(dejah.getNombre()) #Se imprime el valor del metodo Nombre
print(dejah.getEmail()) #Se imprime el valor del metodo Email