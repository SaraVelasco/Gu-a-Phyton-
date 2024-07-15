
#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Di un número: "))

num2 = int(input("Di otro número: "))

operación = (num1/num2)

if num1 > 0:

    print(operación)

else:

    print("ErR0r")    