import math 


print("\n*******Perimetro y Área de un rectángulo*******\n")

Base = float(input("Ingrese la base del rectangulo: "))
Altura = float(input("Ingrese la altura del rectangulo: "))


perimetro = 2*Base + 2*Altura
area = Base * Altura


print("\nEl área del rectángulo es de:", area)
print("El perimetro del rectángulo es de:", perimetro)



print("\n*******Perimetro y Área de un circulo*******\n")

radio = float(input("Ingresa el radio del circulo: "))

areaCirculo = math.pi * pow(radio,2)
perimetroCirculo = 2 * math.pi * radio

print("\nEl área del circulo es de : ",areaCirculo)
print("El perimetro del circulo es de: ",perimetroCirculo)

