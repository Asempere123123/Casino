import random

#Cantidad de veces que se va a realizar la simulacion, subir a 10^7 para la simulacion final
iteraciones = 10000000


#Lista 2d, el primer eje es la carta input y el segundo la carta out, el resultado es el % de que salga esa carta
Veces10 = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0, "22" : 0, "23" : 0, "24" : 0, "25" : 0, "26" : 0, "27" : 0}
Cont10 = 0
#Baraja estandar de blackjack, por motivos de optimizacion esta simplificada. 
# Al todas las cartas estar repetidas 4 veces, la probabilidad de cara carta se mantiene constante(max comun divisor(1, 4) = 4)
Cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

for i in range(0, iteraciones):
    pillaCartas = 0
    
    #Mezclar
    random.shuffle(Cartas)
    
    o = 0
    es = ""

    #Mientras que tengas menos de 17 pillar otra(para el croupier es obligatorio)
    while pillaCartas<17:
        es10 = False

        o += 1
        pillaCartas += Cartas[o]

        if o == 1 and 10 == pillaCartas:
            Cont10 += 1
            es10 = True
            o += 1
            pillaCartas += Cartas[o]
        else: break


        #Cuando coges 2 cartas se determina el valor de la mano inicial
        # y si esta tiene 2 ases, se cuenta uno de los 2 como 1 y el otro como 11(-10)
        if o == 2 and es10 == True:
                Veces10[str(pillaCartas)] += 1
        if o == 2:

            if pillaCartas == 22:
                pillaCartas -= 10
            es = str(pillaCartas)
            break

for i in Veces10:
    Veces10[i] *= 100/Cont10

print(Veces10)