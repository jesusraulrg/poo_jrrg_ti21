"""
  Programa8
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 02/02/2023
  Descripción: unit test
"""

#Realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos y si son iguales imprima NONE

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

if(num1>num2):
    print("El numero mayor es ",num1)
elif(num2>num1):
    print("El numero mayor es ",num2)
else:
    print (None)