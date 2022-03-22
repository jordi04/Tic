class Triangle:
    def __init__(self):
        self.tipo = "Triangulo"
        self.costats = 3
        self.base = 5
        self.altura = 4
        self.area = round(self.base*self.altura/2, 2)

    def console_write_properties(abc):
        print("Tipo: " + abc.tipus)
        print("Lados: " + abc.lados)
        print("Base: " + abc.base)
        print("Altura: " + abc.altura)
    

triangle1 = Triangle()
triangle2 = Triangle()
print("-----Datos del segundo triangulo----")
base = float(input("Longitud de base: "))
altura = float(input("Longitud de altura: "))
triangle2.base = base
triangle2.altura = altura

print("-----Propiedades del primer triangulo-----")
triangle1.console_write_properties()

print("-----Propiedades del segundo triangulo-----")
triangle2.console_write_properties()

if triangle1.area > triangle2.area:
    print("L'àrea del primer triangle és més gran que la del segon triangle")

elif triangle2.area > triangle1.area:
    print("L'àrea del segon triangle és més gran que la del primer triangle")

else: 
    print("Les seves àrees són iguals")


