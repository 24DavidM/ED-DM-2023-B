print("PANADERIA LA UNION")

numGuaguas = int(input("Ingrese el número de guaguas de pan: "))
sumGuaguas = 0.0
sumaMora = 0

for i in range(1,numGuaguas+1,1):
    precioGuagua = float(input(f"Ingrese el precio de la {i} guagua de pan: " ))
    sumGuaguas += precioGuagua
    print("¿La guagua de pan es de mora?")
    tipoGuagua = input("si o no: ")
    if tipoGuagua == "si":
        sumaMora += 1   

print("El total de guaguas son de ",numGuaguas)
print("Precio a pagar $",sumGuaguas)
print("El numero de guaguas de mora son de",sumaMora)