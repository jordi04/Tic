                                                                                                                    import os
import sys
import modul_temps as mt

run = True
pause = False
file = "date_temp.txt" #Si canvies el nom d'aquesta variable, per un arixiu que no existeix, en correr el programa pots escriure el nom d'un altre i així obrir-lo sense error
checking = True
checked = False
clear = lambda: os.system('clear')

while checking == True:
    if mt.fitxer_check(file) == True:
        print("El fitxer existeix. Continuant...")
        checking = False
    else:
        file = input("Insereix el nom del fitxer de text: ")

print(" 0 - Sortir del programa \n 1 - Enregistrar una temperatura i una data aleatòria al fitxer \n 2 - Retornar la temperatura mínima \n 3 - Retornar la temperatura màxima \n 4 - Retornar la temperatura mitjana \n 5 - Imprimeix el text de l'arxiu \n 6 - Per tornar a mostrar aquest missatge \n 7 - Per borrar la consola")

while run == True:
    
    while pause == False:
        while checked == False:
            try:
                entrada = int(input("Insereix un nombre 0-7 (6 per rebre ajuda): "))
            except:
                print("Només pots posar un nombre enter del 0 al 7. \nTorna a intentar-ho")
            else:
                checked = True
                break
        if entrada == 0:
            sys.exit()

        elif entrada == 1:
            mt.add_temp(file)
            checked = False
            
        elif entrada == 2:
            mt.min_temp(file)
            checked = False

        elif entrada == 3:
            mt.max_temp(file)
            checked = False

        elif entrada == 4:
            mt.med_temp(file)
            checked = False

        elif entrada == 5:
            mt.print_temp(file)
            checked = False

        elif entrada == 6:
            print(" 0 - Sortir del programa \n 1 - Enregistrar una temperatura i una data aleatòria al fitxer \n 2 - Retornar la temperatura mínima \n 3 - Retornar la temperatura màxima \n 4 - Retornar la temperatura mitjana \n 5 - Imprimeix el text de l'arxiu \n 6 - Per tornar a mostrar aquest missatge \n 7 - Per borrar la consola")
            checked = False
            
        elif entrada == 7:
            clear()
            checked = False
        else:
            print("Només pots posar un nombre enter del 0 al 7. \nTorna a intentar-ho")
            checked = False
