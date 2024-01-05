num = int(input("Ingresa un número: "))
vacio = 1

for x in range(1, num + 1):
    vacio *= x

print(f"El factorial de {num} es: {vacio}")
