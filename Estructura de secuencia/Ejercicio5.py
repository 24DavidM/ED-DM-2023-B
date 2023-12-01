#DAVID MUELA

nota_parcialUno = float(input("Ingresa tu primera nota del parcial sobre 10: "))
nota_parcialDos = float(input("Ingresa tu segunda nota del parcial sobre 10: "))
nota_parcialTres = float(input("Ingresa tu tercera nota del parcial sobre 10: "))
examenFinal = float(input("Ingresa tu nota del Examen Final: "))
trabajoFinal = float(input("Ingresa tu nota del Trabajo Final: "))

calc_nota = ((nota_parcialUno + nota_parcialDos + nota_parcialTres)/3) * 0.55
calc_examen = examenFinal * 0.30
calc_trabajo = trabajoFinal * 0.15
total = calc_nota + calc_examen + calc_trabajo


print("Tu nota del parcial sobre el 55% es de: ",calc_nota)
print("Tu califacion del examen final sobre el 30% es de: ",calc_examen)
print("Tu califacion del trabajo final sobre el 15% es de: ",calc_trabajo)
print("Tu nota total es de: ",total)

