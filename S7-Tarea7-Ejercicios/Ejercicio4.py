print("\nEscuela Fe y Alegrian")
suma = 0
for i in range(0,4,1):
    while True:
        numero = int(input("Ingresa un nota (Sobre 20): "))
        if numero > 20:
            print("Ingrese correctamente")
        else:
            suma +=numero
            total = suma/4
            break



if total >= 14:
    print("\nAprobado")
elif 13 >= total >= 9:
    print("\nSupletorio")
else:
    print("\nRechazado")
print("El promedio es: ",total)

