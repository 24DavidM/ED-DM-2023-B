#DAVID MUELA

ladoA = int(input("Ingresa tu lado A de un triangulo: "))
ladoB = int(input("Ingresa tu lado B de un triangulo: "))
ladoC = int(input("Ingresa tu lado C de un triangulo: "))


if ladoA == ladoB == ladoC:
    print("El triangulo es equilatero.")
elif ladoA**2 + ladoB**2 == ladoC**2 or ladoA**2 + ladoC**2 == ladoB**2 or ladoB**2 + ladoC**2 == ladoA**2:
    print("El triangulo es rectangulo.")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("El triangulo es isosceles.")
else:
    print("El triángulo es escaleno.")