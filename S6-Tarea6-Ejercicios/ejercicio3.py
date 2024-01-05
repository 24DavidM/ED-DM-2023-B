numeros_pares = 0
numeros_impares = 0

while True:
    numero = int(input("Ingresa un número (o 0 para terminar): "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print("Total de números pares: ",numeros_pares)
print("Total de números impares: ",numeros_impares)
