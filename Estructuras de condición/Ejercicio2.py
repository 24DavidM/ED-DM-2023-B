#DAVID MUELA

nota1 = float(input("Ingresa tu primera nota: "))
nota2 = float(input("Ingresa tu segunda nota: "))
edad = int(input("Ingresa tu edad: "))
sexo = (input("Ingresa tu sexo H o M: "))

if nota1 >= 5 and nota2 >= 5 and edad >= 18:
    if sexo == 'M':
        print("ACEPTADA")
    elif sexo == 'H':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")