"""
  Programa7
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: Calculo del area y perimetro del circulo y el cuadrado
"""

print("Calcula el area y perímetro del círculo y el cuadrado")

pi=3.1416
radio=float(input("Ingresa el valor del radio: "))

perimetro=2*pi*radio
area=pi*radio**2

print ("El perimetro de un círculo de {} de radio {}".format(radio, perimetro))
print ("El area de un círculo de {} de radio {}".format(radio,area))
