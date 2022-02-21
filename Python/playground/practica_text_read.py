nombre_check = True
run = True

while run == True:
    while nombre_check == True:
        nombre = int(input("Insereix un nombre entre 1 i 10: "))
        if nombre >= 1 and nombre <= 10:
            file = "taula-" + str(nombre) + ".txt"
            nombre_check = False
        else:
            continue

    if nombre_check == False:
        try:
            doc = open(file, "r")
        except:
            print("El fitxer no existeix")
            nombre_check = True
        else:
            print(doc.read())
            run = False
