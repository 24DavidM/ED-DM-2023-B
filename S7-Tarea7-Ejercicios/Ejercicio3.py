negativo = int(input("Ingrese un valor negativo: "))
positivo = int(input("Ingrese un valor positivo: "))

suma = 0

for num in range(negativo, positivo + 1):
    suma += num

print(f"La suma de los numeros entre {negativo} y {positivo} es: {suma}")
