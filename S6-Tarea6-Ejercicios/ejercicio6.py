numero = int(input("Ingresa un numero: "))

numero_absoluto = abs(numero)  
contador = 0    
while numero_absoluto > 0:
    numero_absoluto = numero_absoluto // 10
    contador += 1

print("El número",numero,"tiene",contador,"dígitos.")
