#Escribir un programa que pregunte al usuario por el numero de horas trabajadas y el 
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

Número = int(input("¿Cuántas fueron tus horas laborales?"))

Coste = int(input("¿Cuánto cuesta la hora laboral?"))

Total = (Número*Coste)

print("Tu paga es: "+str(Total))



