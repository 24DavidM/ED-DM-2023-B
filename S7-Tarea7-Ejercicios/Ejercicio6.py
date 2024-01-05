def resultado(nombre, creditoActual, TipoTarjeta, creditoAnterior):
    print(" ")
    print("Informacion")
    print("Su nombre es: ", nombre)
    print("Su tipo de Tarjeta es: ", TipoTarjeta)
    print("Su credito anterior es: ", creditoAnterior)
    print("El nuevo crédito para su tarjeta es de:", creditoActual)

print("Banco Pichincha")
nombre = input("Ingresa tu nombre: ")

while True:
    TipoTarjeta = int(input("Ingresa tu tipo de Tarjeta: "))
    creditoAnterior = float(input("Ingrese su crédito actual: "))

    if TipoTarjeta == 1:
        creditoActual = creditoAnterior + (creditoAnterior * 0.25)
        resultado(nombre, creditoActual, TipoTarjeta, creditoAnterior)
        break 
    elif TipoTarjeta == 2:
        creditoActual = creditoAnterior + (creditoAnterior * 0.35)
        resultado(nombre, creditoActual, TipoTarjeta, creditoAnterior)
        break  
    elif TipoTarjeta == 3:
        creditoActual = creditoAnterior + (creditoAnterior * 0.40)
        resultado(nombre, creditoActual, TipoTarjeta, creditoAnterior)
        break  
    elif TipoTarjeta == 4:
        creditoActual = creditoAnterior + (creditoAnterior * 0.50)
        resultado(nombre, creditoActual, TipoTarjeta, creditoAnterior)
        break 
    else:
        print("Tipo de tarjeta no válido (1, 2, 3, 4)")  # Corregí el error tipográfico aquí
