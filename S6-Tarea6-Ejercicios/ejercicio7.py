eleccion = 0
while eleccion != 3:
    eleccion = int(input("Ingresa un numero: "))
    match eleccion:
            case 1:
                print("Comenzando el programa")
                break
            case 2:
                print("Imprimiendo el programa")
                break
            case 3:
                print("Programa Finalizado")
            case other: 
                print("¡ERROR! Ingrese un metodo de calculo disponibe")

