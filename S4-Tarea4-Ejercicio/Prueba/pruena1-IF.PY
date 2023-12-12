print("****BIENVENIDO AL CARBONERO****")
nombre = input("Ingrese su nombre: ")
cedula = int(input("Ingrese su numero de cedula: "))
correo = input("Ingrese su correo electronico: ")

print("Le ofrecemos los siguientes tipos de hamburguesas: ")
print("1. Sencilla")
print("2. Doble")
print("3. Triple")

tipo = int(input("Ingrese el tipo de hamburguesa (num) : "))
num = int(input("Ingrese la cantidad de hamburguesas que desea: "))

if tipo > 3:
   print("Lo sentimos en el CARBONERO no ofrecemos este tipo de hamburguesa")
else:
    if tipo == 1:
        total = 1.50 * num
        print("Por su compra debe cancelar: ", total) 
    elif tipo == 2:
        total = 2.50 * num
        print("Por su compra debe cancelar: ", total) 
    else:
        total = 3.25 * num
        print("Por su compra debe cancelar: ", total) 

    print("Eliga el metodo de pago")
    print("1. Efectivo")
    print("2. Tarjeta de Credito")
    pag = int(input("Ingresa el metodo de pago: "))

    if pag > 2:
        print("El tipo de pago que ingreso no es válido")
    else:
        if pag == 1:
            print("Su pago es en efectivo por favor cancele sin recarga: $",total)
            print(nombre,", muchas gracias por su compra. ¡VUELVA PRONTO!")
            print("La factura sera enviado a su correo: ", correo)
        else:
            iva = 1.05 * total
            print("Su pago es con tarjeta de credito, debera cancelar el 5% adicional del pago:", iva)
            print(nombre, ", muchas gracias por su compra. ¡VUELVA PRONTO!")
            print("La factura sera enviado a su correo: ", correo)
