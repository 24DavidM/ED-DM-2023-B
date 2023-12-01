#DAVID MUELA

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

if numero1 > numero2:
    if numero2 > numero3:
        print("El número",numero1,">",numero2, ">",numero3)
    else: 
        if numero1 > numero3:
            print("El número",numero1, ">",numero3, ">",numero2)
        else:
            print("El número",numero3,">",numero1,">",numero2)
else:
    if numero1 > numero3:
        print("El número",numero2,">", numero1,">", numero3)
    else: 
        if numero3 > numero2:
            print("El número",numero3,">", numero2,">", numero1)
        else:
            print("El número",numero2,">", numero3,">", numero1)