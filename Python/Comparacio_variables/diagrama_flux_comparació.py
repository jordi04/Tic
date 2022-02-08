a = input("Insereix el primer nombre: ")
b = input("Insereix el segon nombre: ")
c = input("Insereix el tercer nombre: ")

a = int(a)
b = int(b)
c = int(c)

g = 0
p = 0

if a == b and b == c:
    print("Tots els nombres són iguals")
else:
    if a == b:
        print("Els dos primers nombres són iguals")
    elif a == c:
        print("Els primer i el tercer nombre són iguals")
    elif c == b: 
        print("Els segon i el tercer nombre són iguals")

    if a > b:
        if a > c:
            g = a
            if b < c:
                p = b
            else:
                p = c
        else: 
            g = c
            if a < b:
                p = a
            else: 
                p = b
    else:
        if b > c:
            g = b
            if b < c:
                p = a
            else: p = c
        else:
            g = c
            if a < b:
                p = a
            else: 
                p = b

    g = str(g)
    p = str(p)
    print("El més gran és: " + g, "El més petit és: " + p)