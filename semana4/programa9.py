"""
  Programa9
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 07/02/2023
  Descripción: Distintas formas de realizar el programa8.py
"""
#Realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos y si son iguales imprima NONE

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

#FORMA_1
if num1>num2:
    print(num1)
if num2>num1:
    print(num2)
if num1==num2:
    print(None)

#Forma_2
if num2>num1:
    print(num2)
if num1>num2:
    print(num1)
else:
    print(None)

#Forma_3
if num1>num2:
    print(num1)
elif num2>num1:
    print(num2)
else:
    print(None)

#Forma_4
if num1==num2:
    print(None)
elif num1>num2:
    print(num1)
elif num2>num1:
    print(num2)

#Forma_5
if num1<num2:
    print(num2)
if num2<num1:
    print(num1)
if num1==num2:
    print(None)

#Forma_6
if num2>num1:
    print(num2)
if num2<num1:
    print(num1)
else:
    print(None)

#Forma_7
if num2<num1>num2:
    print(num1)
elif num1<num2>num1:
    print(num2)
else:
    print(None)

#Forma_8 (programa8)
if num1>num2:
    print(num1)
elif num2>num1:
    print(num2)
else:
    print (None)

#Forma_9

#Forma_10

#Forma_11