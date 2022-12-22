import random
iteraciones = 1000000
media = 0
mediaValor = 0

cant12 = 0
val12 = 0

sumCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
vecesCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
Cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
for i in range(0, iteraciones):
    pillaCartas = 0
    
    #Mezclar
    random.shuffle(Cartas)
    
    o = 0
    es = ""
    while pillaCartas<17:
        o += 1
        pillaCartas += Cartas[-o]
        if o == 2:
            mediaValor += Cartas[-(o+1)]/iteraciones

            if (pillaCartas == 12):
                cant12+=1
                val12 += Cartas[-(o+1)]

            if pillaCartas == 22:
                pillaCartas -= 10
            es = str(pillaCartas)
            vecesCarta[es] += 1
            
    if (pillaCartas <22):
        sumCarta[es] += pillaCartas
    else:
        vecesCarta[es] -=1
    media += pillaCartas/iteraciones

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