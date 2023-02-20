"""
  Programa10
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 09/02/2023
  Descripción: Varias pruebas de escritorio a la vez
"""

def mayor(numero1,numero2): #DEF es una función que evalua dos variables en este caso
    result=None #Declaración de la variable result como NONE POR DEFECTO
    if numero1>numero2: #Si la condición de IF se cumple
        result=numero1 #Entonces result toma el valor del primer valor como verdadero
    elif numero2>numero1: #Si IF no se cumple, se ejecuta ELIF
        result=numero2 #Si ELIF es la condición TRUE, entonces result toma el valor de numero2
    return result #RETURN forma parte de la estructura de la función

#La siguiente lista de PRINT, realiza la comparación del numero mayor imprimiendolo en pantalla con diferentes variables
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #NONE
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #NONE
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1

#PYTHONIC
def mayor(numero1:int,numero2:int)->int|None: #los dos puntos e int se denomina TYPING | los numeros solicitados deben ser enteros
        result=None #None es el valor de la variable por defecto
        if numero1>numero2: #Si la condición se cumple
            result=numero1 #La variable result, toma el valor de numero1 como verdadero
        elif numero2>numero1: #Sino se ejecuta ELIF
            result=numero2 #Si ELIF se cumple, result toma el valor de la variable numero2
        return result #RESULT nos regresa el valor de la variable verdadera

print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #NONE
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #NONE
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1