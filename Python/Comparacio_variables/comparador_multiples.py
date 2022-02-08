# -_- coding:UTF-8 -*-

print("COMPARADOR DE MÚLTIPLES")
a, b = int(input("Insereix el primer nombre: ")), int(input("Insereix el segon nombre: "))

if a > b:
    x = a % b

    if x == 0:
        print(str(a) + " és múltiple de " + str(b))

    else:
        print(str(a) + " no és múltiple de " + str(b))

else:
    x = b % a

    if x == 0:
        print(str(b) + " és múltiple de " + str(a))

    else:
        print(str(b) + " no és múltiple de " + str(a))
