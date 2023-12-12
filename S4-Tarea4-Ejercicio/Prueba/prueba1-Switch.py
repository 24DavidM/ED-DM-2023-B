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

def valor():
    print("Eliga el metodo de pago")
    print("1. Efectivo")
    print("2. Tarjeta de Credito")
    pag = int(input("Ingresa el metodo de pago: "))
    match pag:
        case 1:
            print("Su pago es en efectivo por favor cancele sin recarga: $",total)
            print(nombre,", muchas gracias por su compra. ¡VUELVA PRONTO!")
            print("La factura sera enviado a su correo: ", correo)
        case 2:
            iva = 1.05 * total
            print("Su pago es con tarjeta de credito, debera cancelar el 5% adicional del pago:", iva)
            print(nombre, ", muchas gracias por su compra. ¡VUELVA PRONTO!")
            print("La factura sera enviado a su correo: ", correo)

        case other: print("El tipo de pago que ingreso no es válido")

match tipo:
    case 1:
        total = 1.50 * num
        print("Por su compra debe cancelar: ", total) 
        valor()
    case 2:
        total = 2.50 * num
        print("Por su compra debe cancelar: ", total) 
        valor()
    case 3:
        total = 3.25 * num
        print("Por su compra debe cancelar: ", total) 
        valor()

    case other: print("Lo sentimos en el CARBONERO no ofrecemos este tipo de hamburguesa")

