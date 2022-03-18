class Triangle:
    def __init__(self, tipus, costats, base, altura):
        self.tipus = tipus
        self.costats = costats
        self.base = base
        self.altura = altura
        self.area = round(base*altura/2, 2)

    def console_write_properties(par):
        print("Tipus: " + par.tipus + "\n" + "Costats: " + str(par.costats) + "\n" + "Base: "  + str(par.base) + "\n" + "Altura: " +str(par.altura) + "\n" + "Àrea: "+str(par.area))
    

triangle1 = Triangle("Triangle", 3, 5, 4)
print("-----Dades del segon triangle----")
triangle2 = Triangle("Triangle", 3, float(input("Longitud de la Base: ")), float(input("Longitud de l'Altura: ")))

print("\n-----Propietats del primer triangle-----")
triangle1.console_write_properties()
print("\n-----Propietats del segon triangle-----")
triangle2.console_write_properties()

if triangle1.area > triangle2.area:
    print("L'àrea del primer triangle és més gran que la del segon triangle")

elif triangle2.area > triangle1.area:
    print("L'àrea del segon triangle és més gran que la del primer triangle")

else: 
    print("Les seves àrees són iguals")


