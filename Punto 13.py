
#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
#introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
#mayúsculas y minúsculasntroducida por el usuario coincide con la guardada en la variable sin tener en cuenta
#mayúsculas y minúsculas



contraseña = "VivaSEna45"


contraseña2 = input("Introduce la contraseña: ")


if contraseña.lower() == contraseña2.lower():

    print("La contraseña introducida es correcta.")

else:

    print("La contraseña introducida es incorrecta.")
