
#16. Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por comas

Numberr = int(input("Ingrese un Numero entero positivo :) "))

if Numberr > 0:

    impaRes = {str(i) for i in range (1, Numberr +1 ) if i % 2 != 0}

    print(",".join(impaRes))

else:

    print("No sAbE lEeR?")    