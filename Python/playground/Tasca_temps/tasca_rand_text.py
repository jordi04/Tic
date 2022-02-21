import modul_temps as mt

run = True
pause = False
file = "date_temp.txt"
checking = True

while checking == True:
    if mt.fitxer_check(file) == True:
        print("El fitxer existeix. Continuant...")
        checking = False
    else: 
        print("El fitxer no existeix")
        continue

print(" 0 - Sortir del programa \n 1 - Enregistrar una temperatura i una data aleatòria al fitxer \n 2 - Retornar la temperatura mínima \n 3 - Retornar la temperatura màxima \n 4 - Retornar la temperatura mitjana \n 5 - Imprimeix el text de l'arxiu \n 6 - Per tornar a mostrar aquest missatge")
entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
while run == True:
    while pause == False:
        if entrada == 0:
            run = False
        elif entrada == 1:
            mt.add_temp()
        elif entrada == 2:
            mt.min_temp()
        elif entrada == 3:
            mt.max_temp()
        elif entrada == 4:
            mt.med_temp
        elif entrada == 5:
            mt.print_temp
        elif entrada == 6:
            mt.help()
        else: 
            print("Només pots posar un nombre del 0 al 6. \nTorna a intentar-ho")