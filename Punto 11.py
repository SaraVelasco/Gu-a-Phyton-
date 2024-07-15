#Una panadería vende barras de pan a $ 3.49 pesos cada una. El pan que no es el
#día tiene un descuento del 60%. Escribir un programa que comience leyendo el número
#de barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
#final total.

precio = 3.49

descuento = 0.6 #60%

Barras_viejas = int(input("¿Cuántas barras se vendieron? "))

Con_d = (precio*(1-descuento))

total = (Con_d*Barras_viejas)

print(f"El precio habitual es de: ${precio:.2f} pesos, pero por ser ViEj0 se le aplica un descuento del: {descuento*100:.0f}% y su coste total sería de: ${total:.2f} pesos. :)") 