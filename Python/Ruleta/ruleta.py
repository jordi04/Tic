import random
import tkinter as tk
from tkinter import *

global continua
vint = deu = cinc = tres = un = continua = premi = False
resultat = (random.randrange(0, 101))
bet = input("On apostes? (1, 3, 5, 10, 20) ")
#run = False
bet = int(bet)
x = input("Quant apostes? ")


#print (type(x))

x = int(x)

if resultat <= 4:
    vint = True
    print("Ha sortit 20!")
    
    continua = False
            
elif resultat > 4 and resultat <= 12:
    deu = True
    print("Ha sortit 10!")
    
    continua = False
            
elif resultat > 12 and resultat <= 28:
    cinc = True
    print("Ha sortit 5!")
    
    continua = False
            
elif resultat > 28 and resultat <= 52:
    tres = True
    print("Ha sortit 3!")
    
    continua = False
            
elif resultat > 52 and resultat <= 100:
    un = True
    print("Ha sortit 1!")
    
    continua = False

#AQUÍ COMPROVAM SI EL RESULATAT COINCIDEIX AMB L'APOSTAT

if bet == 20:
    if vint == True:
        print("Has guanyat: ")
        print(x*21)
        premi = True
        continua = False
elif bet == 10:      
    if resultat > 4 and resultat <= 12:
        print("Has guanyat: ")
        print(x*11)
        premi = True
        continua = False
elif bet == 5:
    if resultat > 12 and resultat <= 28:
        print("Has guanyat: ")
        print(x*6)
        premi = True
        continua = False
elif bet == 3:      
    if resultat > 28 and resultat <= 52:
        print("Has guanyat: ")
        print(x*4)
        premi = True
        continua = False
elif bet == 1:
    if resultat > 52 and resultat <= 100:
        print("Has guanyat: ")
        print(x*2)
        premi = True
        continua = False

if premi == False: 
    print("No has guanyat res.")
    #x = input("Quant apostes? ")
if continua == False:
    pass
continua = True 
