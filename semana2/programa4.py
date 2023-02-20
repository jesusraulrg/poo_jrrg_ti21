"""
  Programa4
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 26/01/2023
  Descripción: Diferentes errores con variables
"""

numero1 = 10 #Declaracion de una variable
numero2 = 5 #Declaracion de una variable

print("{}+{}={}".format(numero1,numero2,numero1+numero2)) #Imprime las variables numero1 y numero2 concatenadas con el resultado de la operacion
print("{}+{}=".format(numero1,numero2,numero1+numero2)) #Imprime las variables numero1 y numero2 concatenadas
print("{n1}+{n2}={suma}".format(n1=numero1, n2=numero2, suma=numero1+numero2)) #Imprime el resultado de la operación de variables creadas a partir de otras variables
print("{n2}+{n2}={n2}".format(n1=numero1, n2=numero2, suma=numero1+numero2)) # A pesar de estar todas las varibales, solo toma en cuenta una

#print("{n4}+{n4}={n4}".format(n1=numero1, n2=numero2, suma=numero1+numero2)) Si no exite una varible asignada, marca KeyError
#print("{numero1}+{numero2}={}".format(n1=numero1, n2=numero2, suma=numero1+numero2)) Marca KeyError