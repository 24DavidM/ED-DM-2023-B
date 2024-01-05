print("***ALMACEN LA GANGA***")
print("1. Perfumeria")
print("2. Joyeria")
print("3. Maquillaje")
print("4. Ropa")
print("0. Salir")
total = 0
categoria = int(input("Tipo de Categoria: "))
while categoria != 0:
    if categoria == 1:
        subtotal = 0
        print("1. Tentacion $30")
        print("2. Primavera $28")
        print("3. Otoño     $15")
        print("4. Seduccion $35")
        print("0. Atras")
        tipo = int(input("Elige un producto: "))
        while tipo != 0:
            if tipo == 1:
                producto1 = 30
                subtotal = subtotal + producto1
            elif tipo == 2:
                producto2 = 28
                subtotal = subtotal + producto2
            elif tipo == 3:
                producto3 = 15
                subtotal = subtotal + producto3
            elif tipo == 4:
                producto4 = 35
                subtotal = subtotal + producto4
            else:
                print("Ingresa correctamente los productos disponibles")
            tipo = int(input("Deseas otro producto (No Ingrese 0 para atras): "))
        print("Subtotal de la Categoria *Perfureria*: $",subtotal)
        total = total + subtotal
    elif categoria == 2:
        subtotal1 = 0
        print("1. Aretes    $7")
        print("2. Collar    $5")
        print("3. Cadena    $20")
        print("4. Pulsera   $15")
        print("0. Atras")
        tipo = int(input("Elige un producto: "))
        while tipo != 0:
            if tipo == 1:
                producto5 = 7
                subtotal1 = subtotal1 + producto5
            elif tipo == 2:
                producto6 = 5
                subtotal1 = subtotal1 + producto6
            elif tipo == 3:
                producto7 = 20
                subtotal1 = subtotal1 + producto7
            elif tipo == 4:
                producto8 = 15
                subtotal1 = subtotal1 + producto8
            else:
                print("Ingresa correctamente los productos disponibles")
            tipo = int(input("Deseas otro producto (No Ingrese 0 para atras): "))
        print("Subtotal de la Categoria *Joyeria*: $",subtotal1)
        total = total + subtotal1

    elif categoria == 3:
        subtotal2 = 0
        print("1. Sombras    $8")
        print("2. Maquillaje $5")
        print("3. Labiales   $4")
        print("4. Rimel      $6")
        print("0. Atras")
        tipo = int(input("Elige un producto: "))
        while tipo != 0:
            if tipo == 1:
                producto9 = 8
                subtotal2 = subtotal2 + producto9
            elif tipo == 2:
                producto10 = 5
                subtotal2 = subtotal2 + producto10
            elif tipo == 3:
                producto11 = 4
                subtotal2 = subtotal2 + producto11
            elif tipo == 4:
                producto12 = 6
                subtotal2 = subtotal2 + producto12
            else:
                print("Ingresa correctamente los productos disponibles")
            tipo = int(input("Deseas otro producto (No Ingrese 0 para atras): "))
        print("Subtotal de la Categoria *Maquillaje*: $",subtotal2)
        total = total + subtotal2

    elif categoria == 4:
        subtotal3 = 0
        print("1. Blusa      $25")
        print("2. Chaqueta   $60")
        print("3. Pantalon   $18")
        print("4. Abrigo     $90")
        print("0. Atras")
        tipo = int(input("Elige un producto: "))
        while tipo != 0:
            if tipo == 1:
                producto13 = 25
                subtotal3 = subtotal3 + producto13
            elif tipo == 2:
                producto14 = 60
                subtotal3 = subtotal3 + producto14
            elif tipo == 3:
                producto15 = 18
                subtotal3 = subtotal3 + producto15
            elif tipo == 4:
                producto16 = 90
                subtotal3 = subtotal3 + producto16
            else:
                print("Ingresa correctamente los productos disponibles")
            tipo = int(input("Deseas otro producto (No Ingrese 0 para atras): "))
        print("Subtotal de la Categoria *Rola*: $",subtotal3)
        total = total + subtotal3

    else:
        print("Ingresa correctamente")
    categoria = int(input("Tipo de Categoria: "))
print("Tu total de la compra es de",total)
        