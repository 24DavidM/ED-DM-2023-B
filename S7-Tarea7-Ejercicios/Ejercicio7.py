
print("Etafashion") 
while True: 
    precioprenda = float(input("Ingrese el precio unitario de la prenda: "))
    cantidad = int(input("Ingrese la cantidad de prendas adquiridas: "))
    total = cantidad * precioprenda
    descuento = 0
    if cantidad < 0:
        print("Ingresa un numero valido de prendas")
    else:
        if cantidad > 20:
            descuento = total * 0.1
        elif cantidad > 10:
            descuento = total * 0.05

        nuevo_total = total - descuento

        if cantidad <= 9:
            print("No hay descuento para cantidades menores o iguales a 9 unidades.")
            print("Valor a pagar :$",total)
        else:
            print("Nuevo valor a pagar: $",nuevo_total)
            print("Cantidad de prendas adquiridas: ",cantidad)
    break