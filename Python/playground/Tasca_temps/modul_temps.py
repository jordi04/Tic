import random

def fitxer_check(file):
    try:
        doc = open(file, "r")
    except:
        print("El fitxer no existeix")
        return False
    else:
        doc.close
        return True
def add_temp(file):
    rand_date = str(random.randrange(1,29)) + "/" + str(random.randrange(1,13)) + "/" + str(random.randrange(2010,2023))
    rand_num = str(float(random.randrange(-100,400) / 10)) 
    doc = open(file, "a")
    doc.write(rand_date + ";" + rand_num + "\n")
    doc.close()
    
def min_temp(file):
    lines = []
    data = []
    temp = []
    with open(file) as doc:
        lines = doc.readlines()
    count = 0
    for line in lines:
        count += 1
        #print("Linia: " + str(line) + str(count))
        line = line[0:-1]
        x = line.split(";")
        data.append(x[0])
        temp.append(x[1])
    for i in range(0, len(temp)):
        temp[i] = float(temp[i])
    minima = min(temp)
    index = temp.index(minima)
    print("La temperatura mínima és de " + str(temp[index]) + " ºC de dia " + str(data[index]))
    doc.close()

    
    
def max_temp(file):
    lines = []
    data = []
    temp = []
    with open(file) as doc:
        lines = doc.readlines()
    count = 0
    for line in lines:
        count += 1
        #print("Linia: " + str(line) + str(count))
        line = line[0:-1]
        x = line.split(";")
        data.append(x[0])
        temp.append(x[1])
    for i in range(0, len(temp)):
        temp[i] = float(temp[i])
    maxima = max(temp)
    index = temp.index(maxima)
    print("La temperatura màxima és de " + str(temp[index]) + " ºC de dia " + str(data[index]))
    doc.close()
    
def med_temp(file):
    lines = []
    data = []
    temp = []
    with open(file) as doc:
        lines = doc.readlines()
    count = 0
    for line in lines:
        count += 1
        #print("Linia: " + str(line) + str(count))
        line = line[0:-1]
        x = line.split(";")
        data.append(x[0])
        temp.append(x[1])
    for i in range(0, len(temp)):
        temp[i] = float(temp[i])
    mitjana = round(sum(temp) / len(temp),1)
    print("La temperatura mitjana és de " + str(mitjana) + " ºC")
    doc.close()
    
def print_temp(file):
    doc = open(file, "r")
    print(doc.read())
    
def help():
    print(" 0 - Sortir del programa \n 1 - Enregistrar una temperatura i una data aleatòria al fitxer \n 2 - Retornar la temperatura mínima \n 3 - Retornar la temperatura màxima \n 4 - Retornar la temperatura mitjana \n 5 - Imprimeix el text de l'arxiu \n 6 - Per tornar a mostrar aquest missatge \n 7 - Per borrar la consola")
    