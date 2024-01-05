talleres = 3 
contadorfuga = 0  

while talleres > 0:
    detectafuga = int(input(f"El taller {talleres} detecta una fuga de gas? (1 = Si o 2 = No) "))
    
    if detectafuga == 1:
        contadorfuga += 1
    talleres -= 1

if contadorfuga > 1:
    print("Se ha detectado una fuga de gas al menos en un taller, se ha enviado una alerta por correo.")
else:
    print("No se detecta ninguna fuga")
