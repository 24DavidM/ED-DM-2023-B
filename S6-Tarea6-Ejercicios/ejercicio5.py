objetivo = 1000
total_ahorrado = 0

cantidad_inicial = float(input("Ingrese la cantidad a ahorrar: "))


if cantidad_inicial < 0:
    print("IMPOSIBLE! Ingresar valores negativa.")
else:
    total_ahorrado += cantidad_inicial

    while total_ahorrado < objetivo:
        cantidad = float(input("Ingrese la cantidad a ahorrar : "))

        if cantidad < 0:
            print("No se permiten cantidades negativas.")
        else:
            total_ahorrado += cantidad

            if total_ahorrado >= objetivo:
                break

    if total_ahorrado >= objetivo:
        print("!!ELICIDADESS¡¡ Has alcanzado tu objetivo de",objetivo, "Total ahorrado: $",total_ahorrado)
