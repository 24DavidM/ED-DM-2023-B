
personal = int(input("Ingrese la cantidad de empleado de la EPN"))
sumaSuedo = 0
sumahora = 0
sumaprofe = 0
for i in range(1,personal+1,1):
    sueldo= float(input(f'Ingrese el sueldo del empleado N{i}: '))
    sumaSuedo += sueldo
    horas= int(input(f'Ingrese el número de horas que ha trabajado el empleado N°{i}: '))
    sumahora += horas
    print("¿El empleado es docente?")
    docente = input("si o no: ")
    if docente == "si":
        sumaprofe +=1

print("La cantidad de empleados que se han registrado son: ",personal)
print("El sueldo de todos los empleados es de",sumaSuedo)
print("El total de horas trabajadas de los empleados es de",sumahora)
print("La cantidad de empleados que son docentes son: ",sumaprofe)