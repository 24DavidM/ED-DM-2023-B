#DAVID MUELA

print("*********Viaje Escolar*********")

estudiante = int(input("Ingresa el numero de estudiantes en el viaje: "))

if estudiante >= 100:
    print("Cada estudiante debera pagar $65 euros")
    calc1 = estudiante * 65
    print("En total del viaje sera de",calc1)

elif estudiante >=50 and estudiante <=99:
    print("Cada estudiante debera pagar $70 euros")
    calc2 = estudiante * 70
    print("En total del viaje sera de",calc2)

elif estudiante >=30 and estudiante <=49:
    print("Cada estudiante debera pagar $95 euros")
    calc3 = estudiante * 95
    print("En total del viaje sera de",calc3)
else:
    print("En total del viaje sera de 4000 euros")