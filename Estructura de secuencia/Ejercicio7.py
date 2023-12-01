#DAVID MUELA

numero = int(input("Ingresa un número de dos cifras: "))

if 10 <= numero <= 99:
    unidad = numero % 10
    decena = numero // 10
    invertido = unidad * 10 + decena
    print("El número invertido de", numero, "es", invertido)
else:
    print("Incorrecto, ingresa un número de dos cifras")
