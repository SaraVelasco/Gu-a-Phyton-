#Una Metal- mecánica tiene mucho éxito en dos de sus productos: engranes y cilindros.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
#paquete así que deben calcular el peso de los engranes y cilindros que saldrán en cada
#paquete. Cada engrane pesa 112 g y cada cilindro 75 g. Escribir un programa que lea
#el número de engranes y cilindros vendidos en el último pedido y calcule el peso total
#del paquete que será enviado.

cilindros = 75

engrane = 112

venta_de_e = int(input("¿Cuántos engranes se vendieron? "))

venta_de_c = int(input("¿Cuántos cilindros se vendieron? "))

total_e = (engrane*venta_de_e)

total_c = (cilindros*venta_de_c)

print("El peso total del pedido será de: "+str(total_c+total_e))