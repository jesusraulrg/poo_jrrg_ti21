"""
  Programa2
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: Utilizar el comando str.format
"""

variable1 = "Hola" #Variable tipo str (comillas dobles)
variable2 = '619' #Variable tipo int (comillas simples)
print ("{}{}" .format(variable1,variable2)) #.format nos permite imprimir valores sin importar el tipo de dato que estemos utilizando

variable1 = "Hola" #Variable tipo str (comillas dobles)
variable2 = 619 #Variable tipo int (sin comillas)
print ("{}{}".format(variable1,variable2)) #.format nos permite imprimir valores sin importar el tipo de dato que estemos utilizando