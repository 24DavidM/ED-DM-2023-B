lineas=0
digitos="0123456789"
cantidadDigitos=0
Libro = input("Libro: ")
while Libro!="*":
    for caracter in Libro:
        if caracter in digitos:
            cantidadDigitos+=1
    if Libro=="/":
        lineas+=1
        print("Aparecen ", cantidadDigitos, " dígitos en la línea")
        cantidadDigitos=0
    Libro = input("Libro: ")
print("Se leyeron ",lineas," líneas completas")