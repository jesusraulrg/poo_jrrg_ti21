"""
  Programa6
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: Calculo del area y perimetro de un triángulo
"""

print("Calculo del área y perímetro de un triángulo")

base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
lado1=float(input("Ingrese el primer lado: "))
lado2=float(input("Ingrese el segundo lado: "))
lado3=float(input("Ingrese el tercer lado: "))

area=(base*altura)/2
perimetro=lado1+lado2+lado3

print("El area del triangulo es: ",area)
print("El perimetro del triángulo es: ",perimetro)
