"""
  Programa8
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 02/02/2023
  Descripción: unit test
"""

#Realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos y si son iguales imprima NONE

num1=int(input("Ingrese el primer número: ")) #Solicita una variable de tipo entero al usuario
num2=int(input("Ingrese el segundo número: ")) #Solicita una variable de tipo entero al usuario

if(num1>num2): #IF es un condicional
    print("El numero mayor es ",num1) #Si la condición se cumple, imprime en pantalla la variable num1
elif(num2>num1): #ELIF es parte de la estructura de IF, y se ejecuta SOLO CUANDO la condicion de IF no se cumple; si IF se cumple, en automatico, ELIF y ELSE son descartados
    print("El numero mayor es ",num2) #Imprime en pantalla la variable num2, si no se cumple la primera condición de IF
else: #ELSE forma parte de la estructura de IF cuando ninguna de las primeras condiciones no se cumple
    print (None) #None hace referencia a que ninguna de las condiciones anteriores se cumplió