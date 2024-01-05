numero = int(input("Ingresa un numero: "))
suma=0

if (numero > 0):
  for i in range(2,numero+1,2):
    print(i)
    suma +=i
else:
  print("Número no válido")

print("La sumatoria de los numeros pares es",suma)