"""
  Programa7
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: Calculo del area y perimetro del circulo y el cuadrado
"""

print("Calcula el area y perímetro del círculo y el cuadrado") #Imprime un texto en pantalla

pi=3.1416 #Define la consante de PI
radio=float(input("Ingresa el valor del radio: ")) #Solicita un numero flotante al usuario y lo almacena en una variable

perimetro=2*pi*radio #Realiza una operación aritmetica con la variable y la constante y se almacena en una nueva variable
area=pi*radio**2 #Realiza una operación aritmetica con la variable y la constante y se almacena en una nueva variable

print ("El perimetro de un círculo de {} de radio {}".format(radio, perimetro)) #Imprime texto en pantalla junto con el resultado de la operación con .format
print ("El area de un círculo de {} de radio {}".format(radio,area)) #Imprime texto en pantalla junto con el resultado de la operación con .format