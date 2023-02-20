"""
  Programa3
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: print y operaciones aritméticas con .format
"""

numero1 = 10 #Variable tipo entero (int)
numero2 = 5 #Variable tipo entero (int)
resultado = numero1 + numero2 #Suma las varibles numero1 y numero2

print (numero1+numero2) #Imprime la suma de las variables numero1 y numero2
print ("{}+{}".format(numero1,numero2)) #Toma las varibales numero1 y numero2 y las concatena como str
print ("{}+{}={}".format(numero1,numero2,numero1+numero2)) #Toma las varibales numero1 y numero2, las concatena como str, las opera y concatena el resultado
print ("{}={}*{}".format(numero1*numero2,numero1,numero2)) #Toma las varibales numero1 y numero2, las opera, imprime el resultado y a este concatena la operacion
print ("El resultado de dividir {}/{} es {}".format(numero1,numero2,numero1/numero2)) #Combina una cadena de caracteres con una operación aritmetica concatenada