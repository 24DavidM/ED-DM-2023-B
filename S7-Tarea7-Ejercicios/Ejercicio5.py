
numero = int(input("Ingrese un numero: "))
if numero < 0:
    print("Ingrese un numero entero positivo")
else:
    if 10 <= numero <= 100:
        print("Se encuentra en el intervalo de |10 - 100|")
    else:
        print("No se encuentra en el intervalo de |10 - 100|")
