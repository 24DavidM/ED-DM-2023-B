#DAVID MUELA

monedas_2euro = int(input("Cantidad de monedas de 2€: "))
monedas_1euro = int(input("Cantidad de monedas de 1€: "))
monedas_50cent = int(input("Cantidad de monedas de 50 céntimos: "))
monedas_20cent = int(input("Cantidad de monedas de 20 céntimos: "))
monedas_10cent = int(input("Cantidad de monedas de 10 céntimos: "))

total_centimos = monedas_2euro * 200 + monedas_1euro * 100 + monedas_50cent * 50 + monedas_20cent * 20 + monedas_10cent * 10

euros = total_centimos // 100
centimos = total_centimos % 100

print("Tienes", euros, "euros y", centimos, "céntimos en total.")
