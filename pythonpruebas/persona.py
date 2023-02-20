"""
  persona.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: FEBRERO 2023
  Descripción: Declaración de una clase y objetos
"""

class Persona: #Creamos la clase Persona
    def __init__ (self): #Constructor de la clase Persona
        print("Persona") #Se imprime texto en pantalla
dejah = Persona() #Instancia de una clase
jhon = Persona() #Instancia de una clase

class Persona: #Creamos una clase
    nombre =  None  #La variable nombre toma el valor de None por defecto
    def __init__ (self): #Constructor de la clase Persona
        print("Persona") #Se imprime Persona en pantalla
dejah = Persona() #Instancia de una clase
print(dejah.nombre) #Imprime la instancia de la clase


#ENCAPSULACIÓN
class Persona: #Creamos una clase
    __nombre = None #La variable  __nombre se volvio privada

    def __init__ (self): #Constructor de la clase Persona
        print("Persona") #Se imprime Persona en pantalla

dejah = Persona() #Instancia de una clase
print(dejah.__nombre) #Imprime la instancia de la clase