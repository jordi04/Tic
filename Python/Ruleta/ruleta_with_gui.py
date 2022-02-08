from cgitb import text
from functools import total_ordering
import random
import tkinter as tk
from tkinter import *
from turtle import color

global continua
global to_twenty
to_twenty = to_ten = to_five = to_three = to_one = continua = premi = False

#bet = input("On apostes? (1, 3, 5, 10, 20) ")
#run = False
final = 0
multiplier = 0
global ammount
ammount = 0
global total
total = 1000
global multiplier_won
multiplier_won = 0
landed = 0
#x = input("Quant apostes? ")
window = Tk()

window.title("Gamble")
window.geometry('350x200')

current_ammount = Label(window, text="Currently gambling " + str(ammount) +" scrap")
current_ammount.grid(column=0, row=0)

info = Label(window, text="Where you gambling?")
info.grid(column=0, row=1)

result = Label(window, text="Your have " + str(total) + " scrap")
result.grid(column=0, row=2)

landed_on = Label(window, text="It landed on " + str(landed))
landed_on.grid(column=0, row=3)

if total <= 0:
    result.configure(text="You lost!")

print(multiplier_won)

def gamble_twenty():
    info.configure(text="Gambling to 20")
    global multiplier
    multiplier = 21
    to_twenty = True
twenty = Button(window, text="20", command=gamble_twenty, background="red")
twenty.grid(column=4, row=5)

def gamble_ten():
    info.configure(text="Gambling to 10")
    global multiplier
    multiplier = 11
ten = Button(window, text="10", command=gamble_ten, background="purple")
ten.grid(column=4, row=4)

def gamble_five():
    info.configure(text="Gambling to 5")
    global multiplier
    multiplier = 6
five = Button(window, text="5", command=gamble_five, background="blue")
five.grid(column=4, row=3)

def gamble_three():
    info.configure(text="Gambling to 3")
    global multiplier
    multiplier = 4
three = Button(window, text="3", command=gamble_three, background="green")
three.grid(column=4, row=2)

def gamble_one():
    info.configure(text="Gambling to 1")
    global multiplier
    multiplier = 2
one = Button(window, text="1", command=gamble_one, background="yellow")
one.grid(column=4, row=1)

def add_ten():
    global total
    if total >= 10:
        global ammount
        ammount = 10 + ammount
        total = total - 10
        ammount_str = str(ammount)
        current_ammount.configure(text="Currently gambling "+ ammount_str)
        result.configure(text="Your overall balance is " + str(total) + " scrap")

def subtract_ten():
    global ammount
    if ammount >= 10:
        ammount = ammount - 10
        global total
        total = 10 + total
        ammount_str = str(ammount)
        current_ammount.configure(text="Currently gambling "+ ammount_str)
        result.configure(text="Your overall balance is " + str(total) + " scrap")
    
add_ten_btn = Button(window, text="+10", command=add_ten, background="grey")
add_ten_btn.grid(column=3, row=1)

sub_ten_btn = Button(window, text="-10", command=subtract_ten, background="grey")
sub_ten_btn.grid(column=3, row=2)

def add_hun():
    global total
    if total >= 100:
        global ammount
        ammount = 100 + ammount
        total = total - 100
        ammount_str = str(ammount)
        current_ammount.configure(text="Currently gambling "+ ammount_str)
        result.configure(text="Your overall balance is " + str(total) + " scrap")

def subtract_hun():
    global ammount
    if ammount >= 100:
        ammount = ammount - 100
        global total
        total = 100 + total
        ammount_str = str(ammount)
        current_ammount.configure(text="Currently gambling "+ ammount_str)
        result.configure(text="Your overall balance is " + str(total) + " scrap")
    
add_ten_btn = Button(window, text="+100", command=add_hun, background="grey")
add_ten_btn.grid(column=3, row=3)

sub_ten_btn = Button(window, text="-100", command=subtract_hun, background="grey")
sub_ten_btn.grid(column=3, row=4)

def gamble():
    global ammount
    resultat = (random.randrange(0, 101))

    if resultat <= 4:
        multiplier_won = 21
        
            
    elif resultat > 4 and resultat <= 12:
        multiplier_won = 11
        
                
    elif resultat > 12 and resultat <= 28:
        multiplier_won = 6
        
                
    elif resultat > 28 and resultat <= 52:
        multiplier_won = 4
        
                
    elif resultat > 52 and resultat <= 100:
        multiplier_won = 2
    
    landed = multiplier_won - 1
    if multiplier == multiplier_won:
        print(ammount)
        print(multiplier)
        global final
        final = ammount * multiplier
        global total
        total =  final + total
        print(total)
        result.configure(text="Your overall balance is " + str(total) + " scrap")
        
    else:
        result.configure(text="Your overall balance is " + str(total) + " scrap")
    ammount = 0
    current_ammount.configure(text="Currently gambling "+ str(ammount))
    landed_on.configure(text="It landed on "+ str(landed))

gbl = Button(window, text="Spin", command=gamble)
gbl.grid(column=0, row=4)
if ammount == total and ammount == 0:
    print("You lost!")

if to_twenty == True:

    result.configure(text="")
window.mainloop()