#DAVID MUELA

import math 

x1 = int(input("Ingresa un número en tu eje X1: "))
x2 = int(input("Ingresa un número en tu eje X2: "))
y1 = int(input("Ingresa un número en tu eje Y1: "))
y2 = int(input("Ingresa un número en tu eje Y2: "))

distancia = math.sqrt((pow((x2)-(x1),2)) + (pow((y2)-(y1),2)))


print("La distancia que separa ambos puntos en un plano cartesiano es: ",distancia)