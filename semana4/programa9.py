"""
  Programa9
  Nombre: Jesús Raúl Rosas Gómez
  Fecha: 07/02/2023
  Descripción: Distintas formas de realizar el programa8.py
"""
#Realiza un programa que compare 2 numeros enteros e imprima el mayor de ellos y si son iguales imprima NONE

num1=int(input("Ingrese el primer número: ")) #Solicita un numero entero al usuario y lo almacena en la variable
num2=int(input("Ingrese el segundo número: ")) #Solicita un numero entero al usuario y lo almacena en la variable

#FORMA_1
if num1>num2: #IF compara a las variables num1 y num2
    print(num1) #Si la condición se cumple, imprime en pantalla la variable num1
if num2>num1: #Si en la estructura de IF no esta ELIF, todos los condicionales IF se evaluan, así la primera condición se haya cumplido
    print(num2) #Imprime en pantalla la variable num2 si esta se cumple
if num1==num2: #IF compara a las variables num1 y num2 por si estas son iguales
    print(None) #Imprime NONE en pantalla

#Forma_2
if num2>num1: #IF compara a las variables num1 y num2
    print(num2) #Si la condición de IF se cumple, se imprime en pantalla la variable num2
if num1>num2: #IF compara a las variables num1 y num2
    print(num1) #Si la condición de IF se cumple, se imprime en pantalla la variable num1
else: #Si nunguna de las condiciones anteriores de cumple, else es ejecutado
    print(None) #Imprime None

#Forma_3
if num1>num2: #IF compara a las variables num1 y num2
    print(num1) #Si la condición de IF se cumple, se imprime en pantalla la variable num1
elif num2>num1: #Si IF no se cumple, se ejecuta ELIF comparando a las variables en otro orden
    print(num2) #Si la condición de ELIF se cumple, se imprime en pantalla la variable num2
else: #Si ninguna condición se cumple, else se ejecuta
    print(None) #Imprime NONE en pantalla

#Forma_4
if num1==num2: #IF compara si num1 y num2 son iguales
    print(None) #Imprime en pantalla None
elif num1>num2: #Si IF no se cumple, se ejecuta ELIF
    print(num1) #Si ELIF se cumple, se imprime la variable num1
elif num2>num1: #Si el primer ELIF no se cumple, se ejecuta la siguiente condición ELIF
    print(num2) #Si la segunda condición se cumple, se imprime num2 en pantalla

#Forma_5
if num1<num2: #En este caso IF compara las variables en un orden diferente
    print(num2) #Si la condición se cumple, num2 se imprime en pantalla
if num2<num1: #Al ser nuevamente el condicional IF, así la primer condición haya sido verdadera, se ejecuta la siguiente
    print(num1) #Si esta se cumple, num1 se imprime en pantalla
if num1==num2: #Finalmente IF compara a las variables num1 y num2
    print(None) #Si las variables son iguales, se imprime en pantalla la palabra NONE

#Forma_6
if num2>num1: #Se comparan las variables num1 y num2
    print(num2) #Si la condición se cumple, se imprime en pantalla la variable num2
if num2<num1: #Al ser nuevamente el condicional IF, así la primer condición haya sido verdadera, se ejecuta la siguiente
    print(num1) #Si esta se cumple, num1 se imprime en pantalla
else: #Si ninguna variable de las evaluadas se cumple, se ejecuta ELSE
    print(None) #Imprime NONE en pantalla

#Forma_7
if num2<num1>num2: #IF compara si dos condiciones se cumplen
    print(num1) #Si se estas se cumplen, se imprime la variable num1
elif num1<num2>num1: #Si la primer condicion de IF no se cumplió, ahora se ejecuta ELIF
    print(num2) #Se imprime la variable num2 en pantalla su ELIF se cumple
else: #Si ninguna de las condiciones se cumple, else se ejecuta
    print(None) #Se imprime NONE en pantalla

#Forma_8 (programa8)
if num1>num2: #Se comparan las variables num1 y num2
    print(num1) #Si IF es verdadero, se imprime num1 en pantalla
elif num2>num1: #Si no se cumple, se ejecuta ELIF
    print(num2) #Si ELIF se cumple se imprime la variable num2 en pantalla
else: #Si ninguna de las variables se cumple, se ejecuta ELSE
    print (None) #Else imprime NONE en pantalla