print("Programa que si una persona puede conducir o no considerando su edad y si tiene licencia")
print("Ingrese su edad")
edad = int(input())
print("Tiene licencia? (1.si / 2. no)")
licencia = int(input())
if edad >= 18 and licencia == 1:
    print("Puede conducir")
else:
    print("No puede conducir")