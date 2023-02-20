"""
  Programa6
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 24/01/2023
  Descripción: Calculo del area y perimetro de un triángulo
"""

print("Calculo del área y perímetro de un triángulo") #Imprime texto en pantalla

base=float(input("Ingrese la base: ")) #Solicita al usuario un numero flotante y lo almacena en una variable
altura=float(input("Ingrese la altura: ")) #Solicita al usuario un numero flotante y lo almacena en una variable
lado1=float(input("Ingrese el primer lado: ")) #Solicita al usuario un numero flotante y lo almacena en una variable
lado2=float(input("Ingrese el segundo lado: ")) #Solicita al usuario un numero flotante y lo almacena en una variable
lado3=float(input("Ingrese el tercer lado: ")) #Solicita al usuario un numero flotante y lo almacena en una variable

area=(base*altura)/2 #Realiza una operación aritmetica con dos de las variables solicitadas al usuario y las almacena en una nueva
perimetro=lado1+lado2+lado3 #Realiza una operación aritmetica con tres de las variables solicitadas al usuario y las almacena en una nueva

print("El area del triangulo es: ",area) #Imprime texto en pantalla dando el resultado de la operación alojada en una variable
print("El perimetro del triángulo es: ",perimetro) #Imprime texto en pantalla dando el resultado de la operación alojada en una variable
