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

match tip:
    case 1:
        calc = num1 + num2
        print("El resultado de la suma es: ",calc)
    case 2:
        calc = num1 - num2
        print("El resultado de la resta es:", calc)
    case 3:
        calc = num1 * num2
        print("El resultado de la multiplicacion es:", calc)
    case 4:
        if num2 == 0:
            print("¡IMPOSIBLE¡ Dividir para CERO")
        else:
            calc = num1 / num2
            print("El resultado de la division es:", calc)
    case 5:
        if num2 == 0:
            print("¡IMPOSIBLE¡ Dividir para CERO")
        else:
            calc = num1 % num2
            print("El resultado de modulo es:", calc)
    case other: print("¡ERROR! Ingrese un metodo de calculo disponible")



