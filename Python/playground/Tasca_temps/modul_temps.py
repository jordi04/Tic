import random
def fitxer_check(file):
    try:
        doc = open(file, "r")
    except:
            
        file = input("Insereix el nom del fitxer: ")
        return False
    else:
        return True
def add_temp():
    rand_date = str(random.randrange(1,29)) + "/" + str(random.randrange(1,13)) + "/" + str(random.randrange(2010,2023))
    rand_num = str(float(random.randrange(-100,400) / 10)) 
    print(rand_date + ";" + rand_num)

    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
def min_temp():

    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
def max_temp():

    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
def med_temp():

    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
def print_temp():

    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))
def help():
    print(" 0 - Sortir del programa \n 1 - Enregistrar una temperatura i una data aleatòria al fitxer \n 2 - Retornar la temperatura mínima \n 3 - Retornar la temperatura màxima \n 4 - Retornar la temperatura mitjana \n 5 - Imprimeix el text de l'arxiu \n 6 - Per tornar a mostrar aquest missatge")
    entrada = int(input("Insereix un nombre 0-6 (6 per rebre ajuda): "))