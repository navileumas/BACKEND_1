import math
TC = 18
print("PROGRAMA QUE CONVIERTE PESOS A DOLARES")
print("Ingrese la cantidad de pesos que desea convertir a dolares")
pesos = float(input())
dolares = round( pesos / TC, 2)
print("La cantidad de dolares es: ", dolares)