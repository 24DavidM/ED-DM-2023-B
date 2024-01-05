total_pagar = 0

while True:
    monto = float(input("Ingrese el monto de la compra (ingrese 0 para finalizar): "))

    if monto == 0:
        break 
    
    if monto < 0:
        print("El monto no puede ser negativo. Ingrese un monto válido.")
        continue  

    total_pagar += monto 
    descuento = total_pagar - (total_pagar * .10)

if total_pagar >= 1000:
    print("Se le acredito un descuentro del 10% en Total a pagar es $",descuento)
else:
    print("El total a pagar es: ",total_pagar)

