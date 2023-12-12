print("\n---CALCULADORA---")

num1 = float(input("\nIngresa un numero: "))
num2 = float(input("Ingresa otro numero: "))

print("\nQue metodo desea usar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Modulo")

tip = int(input("\nQue metodo desea usar: "))
if tip > 6:
    print("¡ERROR! Ingrese un metodo de calculo disponible")
else:
    if tip == 1:
        calc = num1 + num2
        print("El resultado de la suma es: ",calc)
    elif tip == 2:
        calc = num1 - num2
        print("El resultado de la resta es:", calc)
    elif tip == 3:
        calc = num1 * num2
        print("El resultado de la multiplicacion es:", calc)
    elif tip == 4:
        if num2 == 0:
            print("¡IMPOSIBLE¡ Dividir para CERO")
        else:
            calc = num1 / num2
            print("El resultado de la division es:", calc)
    elif tip == 5:
        if num2 == 0:
            print("¡IMPOSIBLE¡ Dividir para CERO")
        else:
            calc = num1 % num2
            print("El resultado de modulo es:", calc)
