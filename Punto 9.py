#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
#el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
#Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
#calculado redondeado con dos decimales.

Peso = float(input("Introduzca su peso en kilogramos: "))

Altura = float(input("Introduzca su altura en metros: "))

imc = (Peso/(Altura**2))

print(f"Tu imc es: {imc:.2f}")