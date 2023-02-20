"""
  persona.py
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: FEBRERO 2023
  Descripción: Declaración de clases y objetos
"""

class Persona: #Se determina una clase

    __nombre = None #La variable privada nombre toma el valor de None por defecto
    __edad = None #La variable privada edad toma el valor de None por defecto

    def __init__(self): #Función que crea un método
        print("Persona") #Imprime Persona en pantalla

    def setNombre(self,nombre): #Se determina un método de la clase Persona
        self.__nombre = nombre #La variable nombre se vuelve privada
    def getNombre(self): #La función solicita a la variable
        return self.__nombre #Regresa el resultado de la variable como metodo de una clase

    def setEdad(self,edad): #Se determina un método de la clase Persona
        self.__edad = edad #La variable edad se vuelve privada
    def getEdad(self): #La función solicita a la variable
        return self.__edad #Regresa el resultado de la variable como metodo de una clase

class Alumno(Persona): #Se determina una clase heredando los metodos de Persona

    __matricula = None #La variable privada matricula toma el valor de None por defecto
    __nombre = None #La variable privada nombre toma el valor de None por defecto
    
    def __init__(self): #Constructor de la clase Alumno
        super().__init__() #Llama al constructor de la clase Persona
        print ("Alumno") #Imprime Alumno en pantalla

    def setMatricula(self,matricula): #Se determina un método de la clase Alumno
        self.__matricula = matricula #La variable matricula se vuelve privada
    def getMatricula(self): #La función solicita a la variable
        return self.__matricula #Regresa el resultado de la variable como metodo de una clase
    
class Coordinador(Persona): #Se determina una clase heredando los metodos de Persona

    __nomina = None #La variable privada nomina toma el valor de None por defecto
    __carrera = None #La variable privada carrera toma el valor de None por defecto

    def __init__(self): #Constructor de la clase Coordinador
        super().__init__() #Llama al constructor de la clase Persona
        print ("Coordinador") #Muestra el mensaje "Coordinador"

    def setNomina(self,nomina): #Se determina un método de la clase Coordinador
        self.__nomina = nomina #La variable nomina se vuelve privada
    def getNomina(self): #La función solicita a la variable
        return self.__nomina #Regresa el resultado de la variable como metodo de una clase

    def setCarrera(self,carrera): #Se determina un método de la clase Coordinador
        self.__carrera = carrera #La variable carrera se vuelve privada
    def getCarrera(self): #La función solicita a la variable
        return self.__carrera #Regresa el resultado de la variable como metodo de una clase

class Profesor(Persona): #Se determina una clase heredando los metodos de Persona

    __nomina = None #La variable privada nomina toma el valor de None por defecto
    def __init__(self): #Constructor de la clase Profesor
        super().__init__() #Llama al constructor de la clase Persona
        print ("Profesor") #Muestra el mensaje "Profesor"

    def setNomina(self,nomina): #Se determina un método de la clase Profesor
        self.__nomina = nomina #La variable nomina se vuelve privada
    def getNomina(self): #La función solicita a la variable
        return self.__nomina #Regresa el resultado de la variable como metodo de una clase

objeto_persona = Persona() #Se crea la instancia de un objeto
objeto_alumno = Alumno() #Se crea la instancia de un objeto
objeto_profesor = Profesor() #Se crea la instancia de un objeto
objeto_coordinador = Coordinador() #Se crea la instancia de un objeto