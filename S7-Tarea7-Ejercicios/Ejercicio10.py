print("CUENTA DE AHORROS")
def mes():
    mes = int(input("Ingresa un numero del mes (1 al 12) : "))
    if mes == 1:
        print("Enero")
    elif mes == 2:
        print("Febrero")
    elif mes == 3:
        print("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Mayo")
    elif mes == 6:
        print("Junio")
    elif mes == 7:
        print("Julio")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Septiembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Noviembre")
    elif mes == 12:
        print("Diciembre")
    else:
        print("Número de mes no válido")
sumar = 0
while True:
    print("1. Depositar Dinero (Mes)")
    print("2. Consultar Dinero")
    print("0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        mes()
        ahorro = int(input(f"Ingresa el dinero ahorrar en el mes: $" ))
        sumar+=ahorro
    elif opcion == 2:
        print("El ahorro acumulado en este año es de $",sumar)
    elif opcion == 0:
        break
    else:
        print("Ingrese correcamente")