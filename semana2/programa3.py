"""
  Programa3
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: print y operaciones aritméticas con .format
"""
numero1 = 10 #Variable tipo int
numero2 = 5 #Variable tipo in
resultado=numero1+numero2
print (numero1+numero2) #15
print ("{}+{}".format(numero1,numero2)) #10+5
print ("{}+{}={}".format(numero1,numero2,numero1+numero2)) #10+5=15
print ("{}={}*{}".format(numero1*numero2,numero1,numero2))
print ("El resultado de dividir {}/{} es {}".format(numero1,numero2,numero1/numero2))
