

llista_divisibles = []
end = False
inici = True

#LOOP QUE DEMANA UN NOMBRE POSITIU O ZERO PER CONTINUAR
while inici == True:
    x = int(input("Escriu un nombre major que zero (o posa 0 per sortir): "))
    if x < 0:
        print("El nombre ha de ser major que zero!")
    else:
        inici = False
        break

#WHILE LOOP QUE S'EXECUTARÀ SI EL NOMBRE DONAT ÉS >= 0 
while inici == False:
    #IF PER ACABAR EL PROGRAMA QUAN EL NOMBRE ÉS ZERO
    if x == 0:
        end = True

    #AQUEST IF S'EXECUTARÀ SEMPRE QUE EL CODI HAGI D'ACABAR
    if end == True:
        print("Gràcies per emprar aquest programa")
        break

    #AQUÍ ES CALCULEN I S'AFAGEIXEN ELS DIVISORS DEL NOMBRE DONAT A UNA LLISTA
    for y in range(1,x+1):
        if x%y == 0:
            llista_divisibles.append(y)

    if llista_divisibles[-1] == x:
        #AQUÍ ES REVISA SI ÉS UN NOMBRE PRIMER O NO
        if len(llista_divisibles) <= 2:
            print(str(x) + " és un nombre primer")
            end = True
        else:
            #AQUESTA PART CONVERTEIX LA LLISTA EN STRING PER PODER CANVIAR LA DARRERA COMA PER UNA i I ELIMINAR ELS CLAUDATORS
            llista_divisibles_str = str(llista_divisibles)
            llista_divisibles_comma = llista_divisibles_str.rfind(",")
            llista_divisibles_str = (llista_divisibles_str[:llista_divisibles_comma] + " i" + llista_divisibles_str[llista_divisibles_comma+1:])
            llista_divisibles_str = (llista_divisibles_str).replace("[","")
            llista_divisibles_str = llista_divisibles_str.replace("]","")
            
            #AQUÍ S'IMPRIMEIX EL RESULTAT
            print("Els " + str(len(llista_divisibles)) + " divisors de " + str(x) + " són: " + llista_divisibles_str)
            end = True
