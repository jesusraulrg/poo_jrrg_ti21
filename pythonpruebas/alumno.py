"""
  alumno.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: FEBRERO 2023
  Descripción: Declaración de una clase y metodos
"""

class Alumno: #Declaracion de una clase

    __nombre = None #Variable de tipo privada, toma el valor None por defecto en la estructura antes de ser ejecutado el resto del programa
    __matricula = None #Variable de tipo privada, toma el valor None por defecto en la estructura antes de ser ejecutado el resto del programa
    __carrera = None #Variable de tipo privada, toma el valor None por defecto en la estructura antes de ser ejecutado el resto del programa

    def __init__(self): #Función que crea un método
        print("Alumno") #Imprime Alumno en pantalla

    def setNombre(self,nombre): #Se determina un método de la clase Alumno
        self.__nombre = nombre #La variable nombre se vuelve privada
    def getNombre(self): #La función solicita a la variable
        return self.__nombre #Regresa el resultado de la variable como metodo de una clase

    def setMatricula(self,matricula): #Se determina un método de la clase Alumno
        self.__matricula = matricula #La variable matricula se vuelve privada
    def getMatricula(self): #La función solicita a la variable
        return self.__matricula #Regresa el resultado de la variable como metodo de una clase
    
    def setCarrera(self,carrera): #Se determina un método de la clase Alumno
        self.__carrera = carrera #La variable carrera se vuelve privada
    def getCarrera(self): #La función solicita a la variable
        return self.__carrera #Regresa el resultado de la variable como metodo de una clase

jesus = Alumno() #Determinación de la clase
jesus.setNombre("Jesús") #Se determina el valor del método Nombre
jesus.setMatricula("1722110013") #Se determina el valor del método Matricula
jesus.setCarrera("TICS") #Se determina el valor del método Carrera
print(jesus.getNombre()) #Se imprime en pantalla el valor de Nombre dentro de su clase
print(jesus.getMatricula()) #Se imprime en pantalla el valor de Matricula dentro de su clase
print(jesus.getCarrera()) #Se imprime en pantalla el valor de Carrera dentro de su clase