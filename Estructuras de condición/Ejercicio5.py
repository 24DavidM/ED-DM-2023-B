#DAVID MUELA

tipo = input("Ingrese el tipo A o B  de uva : ")
tamaño = int(input("Ingrese el tamaño 1 o 2 de la uva : "))

precio_inicial = 10  
factor_cambio = 0

if tipo == "A":
    if tamaño == 1:
        factor_cambio = 0.20
    else:
        factor_cambio = 0.30
else:
    if tamaño == 1:
        factor_cambio = -0.30
    else:
        actor_cambio = -0.50

ganancia = precio_inicial + (precio_inicial * factor_cambio)
    
print("La ganancia obtenida es:",ganancia)


