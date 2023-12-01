#DAVID MUELA

def dimeTipoMotor():

    tipo_motor = int(input("Ingrese el tipo de motor (valores posibles: 1, 2, 3, 4): "))

    if tipo_motor == 0:
        mensaje = "No hay establecido un valor definido para el tipo de bomba"
    elif tipo_motor == 1:
        mensaje = "La bomba es una bomba de agua"
    elif tipo_motor == 2:
        mensaje = "La bomba es una bomba de gasolina"
    elif tipo_motor == 3:
        mensaje = "La bomba es una bomba de hormigón"
    elif tipo_motor == 4:
        mensaje = "La bomba es una bomba de pasta alimenticia"
    else:
        mensaje = "No existe un valor válido para tipo de bomba"
        
    print(mensaje)

dimeTipoMotor()
