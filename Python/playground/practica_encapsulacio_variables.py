from curses.textpad import rectangle
from re import X


class Rectangle():
    def __init__(self):
        self.costats = 4
        self.base = 0
        self.altura = 0
    
    def definir(self, base, altura):
        self.base = base
        self.altura = altura
    
    def propietats(par):
        print("Costats: " + str(par.costats) + "\n" + "Base: "  + str(par.base) + "\n" + "Altura: " +str(par.altura))
    
    def area(par):
        print("Àrea: "+str(par.base*par.altura))

    def perimetre(par):
        print("Perímetre: " + str(2*par.base+2*par.altura))

def check(numero):
    try: 
        numero = float(numero)
    
    except:
        return False

    else:
        if (numero > 0):
            return True
        else:
            return False

rectangle1 = Rectangle()

x_base = input("Valor de la base: ")
while check(x_base) == False:
    print("Fora de rang")
    x_base = input("Introdueix el valor de la base: ")
x_base = float(x_base)

x_altura = input("Valor de l'altura: ")
while check(x_altura) == False:
    print("Fora de rang")
    x_altura = input("Introdueix el valor de l'altura: ")
x_altura = float(x_altura)

rectangle1.base = x_base
rectangle1.altura = x_altura

rectangle1.propietats()
rectangle1.area()
rectangle1.perimetre()
        