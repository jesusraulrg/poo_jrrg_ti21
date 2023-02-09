"""
  Programa10
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 09/02/2023
  Descripción: Pruebas de escritorio a la vez
"""

def mayor(numero1,numero2):
    result=None
    if numero1>numero2:
        result=numero1
    elif numero2>numero1:
        result=numero2
    return result
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #NONE
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #NONE
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1

#PYTHONIC
def mayor(numero1:int,numero2:int)->int|None: #los dos puntos e int se denomina TYPING |
        result=None
        if numero1>numero2:
            result=numero1
        elif numero2>numero1:
            result=numero2
        return result
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #NONE
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #NONE
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1
