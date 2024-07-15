#Escribir un programa que lea un entero positivo, n , introducido por el usuario y después
#muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los primeros
#enteros positivos puede ser calculada de la siguiente forma:

Número = int(input("Introduzca un número entero positivo: "))

if Número > 0:

  Total = Número*(Número+1)//2

  print("la suma de lo primeros enteros positivos es: "+str(Total))


else:

  print("No es un número entero positivo")

