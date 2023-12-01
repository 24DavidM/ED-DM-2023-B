#DAVID MUELA

distancia = float(input("Ingrese la distancia entre los vehículos en kilómetros: "))
velocidadUno = float(input("Ingrese la velocidad del primer vehículo en km/h: "))
velocidadDos = float(input("Ingrese la velocidad del segundo vehículo en km/h: "))


if velocidadUno > velocidadDos:
    tiempo_minutos = distancia / (velocidadDos + velocidadUno) * 60
    if tiempo_minutos > 0:
        print("El vehículo más rápido alcanzará al otro en",tiempo_minutos,"minutos.")
else:
    print("El vehículo más rápido no alcanzará al otro.")