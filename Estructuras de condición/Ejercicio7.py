#DAVID MUELA

print("Compañia de Transporte")

paquete = float(input("Ingrese el peso del paquete maximo hasta 5kg: "))

print("Lugar disponibles de Envio")
print("1. America del Norte")
print("2. America Central")
print("3. America del Sur")
print("4. Europa")
print("5. Asia")

ubicacion = int(input("Eliga el lugar de destino a enviar: "))

if ubicacion <= 5:
    if paquete <= 5:
        if ubicacion == 1:
            print("Se ha enviado correctamente su paquete")
            costo1 = paquete * 24
            print("El costo del paquete sera de $",costo1,"euros")
        elif ubicacion ==2:
            print("Se ha enviado correctamente su paquete")
            costo2 = paquete * 20 * 1000
            print("El costo del paquete sera de $",costo2,"euros")
        elif ubicacion ==3:
            print("Se ha enviado correctamente su paquete")
            costo3 = paquete * 21 * 1000
            print("El costo del paquete sera de $",costo3,"euros")
        elif ubicacion ==4:
            print("Se ha enviado correctamente su paquete")
            costo4 = paquete * 10 * 1000
            print("El costo del paquete sera de $",costo4,"euros")
        elif ubicacion ==5:
            print("Se ha enviado correctamente su paquete")
            costo5 = paquete * 18 * 1000
            print("El costo del paquete sera de $",costo5,"euros")
    else:
        print("El peso maximo establecido es de 5kg")
else:
    print("Ingrese correctamente un sitio disponible")