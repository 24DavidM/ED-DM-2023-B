#DAVID MUELA
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
ventas = float(input("Ingrese el monto total de las tres ventas del mes: "))

comision_por_venta = 0.10 * ventas
total_comisiones = comision_por_venta * 3
total_mes = sueldo_base + total_comisiones

print("El dinero obtenido por comisiones en las ventas en el mes es: ",total_comisiones)
print("El total que recibirá en el mes, considerando su sueldo base y comisiones es: ",total_mes)
