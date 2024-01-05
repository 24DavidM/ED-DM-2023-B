def menu():
    print("1. Power")
    print("2. Menu ")
    print("3. Arriba ↑")
    print("4. Abajo ↓")
    print("5. Izquierda ←")
    print("6. Derecha →")
    print("7. Smart TV")
    print("8. Multi")
    print("9. Option")
    print("10. Desconectar")
    
control = int(input("Ingresa un accion a realizar el control SMART TV: "))
menu()
while control != 10:
    if control == 1:
        print("Encendiendo el dispositivo TV")
    elif control == 2:
        print("Ingresando al menu del Televisor")
    elif control == 3:
        print("Moviendo la pantalla para Arriba")
    elif control == 4:
        print("Moviendo la pantalla para Abajo ↓")
    elif control == 5:
        print("Moviendo la pantalla para Izquierda ←")
    elif control == 6:
        print("Moviendo la pantalla para Derecha →")
    elif control == 7:
        print("Ingresando a la informacion del Televisor")
    elif control == 8:
        print("Ingresando a los archivos multimedias")
    elif control == 9:
        print("Ingresando a la configuracion del dispositivo Electronico")
    elif control == 10:
        print("10. Apagando el Televisor")
    else:
        print("Número de control no válido o no funcional")
    control = int(input("Ingresa un accion a realizar el control SMART TV: "))

