import random

#Cantidad de veces que se va a realizar la simulacion, subir a 10^7 para la simulacion final
iteraciones = 1000

media = 0
mediaValor = 0

cant12 = 0
val12 = 0

sumCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
vecesCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}

#Baraja estandar de blackjack, por motivos de optimizacion esta simplificada. Al todas las cartas estar repetidas 4 veces, la probabilidad de cara carta se mantiene constante(max comun divisor(1, 4) = 4)
Cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

for i in range(0, iteraciones):
    pillaCartas = 0
    
    #Mezclar
    random.shuffle(Cartas)
    
    o = 0
    es = ""

    #Mientras que tengas menos de 17 pillar otra(para el croupier es obligatorio)
    while pillaCartas<17:

        o += 1
        pillaCartas += Cartas[-o]

        #Cuando coges 2 cartas se determina el valor de la mano inicial
        # y si esta tiene 2 ases, se cuenta uno de los 2 como 1 y el otro como 11(-10)
        if o == 2:
            mediaValor += Cartas[-(o+1)]/iteraciones

            if (pillaCartas == 12):
                cant12+=1
                val12 += Cartas[-(o+1)]

            if pillaCartas == 22:
                pillaCartas -= 10
            es = str(pillaCartas)
            vecesCarta[es] += 1

    #Codigo para sacar el resultado del bucle for(que se ejecuta cada simulación)  
    if (pillaCartas <22):
        sumCarta[es] += pillaCartas
    else:
        vecesCarta[es] -=1
    media += pillaCartas/iteraciones


#Codigo que organiza el resultado y lo expone de una forma mas sencilla de interpretar
carta = []
i = 1
for a, v in sumCarta.items():
    if vecesCarta[a] != 0:
        carta.append({i : sumCarta[a]/vecesCarta[a]})
    else:
        carta.append({i : 0})
    i += 1

print(carta)
print(media, mediaValor)
print(val12/cant12)