suma_notas = 0
cantidad_notas = 0


nota = float(input("Ingresa una nota (ingresa 0 para terminar): "))
while nota != 0:
    suma_notas += nota
    cantidad_notas += 1
    nota = float(input("Ingresa una nota (ingresa 0 para terminar): "))

promedio = suma_notas / cantidad_notas
print("El promedio de las notas ingresadas es: ",promedio)