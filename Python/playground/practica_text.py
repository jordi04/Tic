nombre_check = True
write = True

while nombre_check == True:
    nombre = int(input("Insereix un nombre entre 1 i 10: "))
    if nombre >= 1 and nombre <= 10:
        file = "taula-" + str(nombre) + ".txt"
        nombre_check = False
        break
    else:
        continue

if write == True:
    doc = open(file, "w")

    for i in range(1,11):
        content = str(nombre) +  "x" + str(i) + " = " + str(nombre * i) + "\n"
        doc.write(content)
    doc.close()
