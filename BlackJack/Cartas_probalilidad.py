import random
iteraciones = 1000000
media = 0

sumCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
vecesCarta = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0, "13" : 0, "14" : 0, "15" : 0, "16" : 0, "17" : 0, "18" : 0, "19" : 0, "20" : 0, "21" : 0}
Cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
for i in range(0, iteraciones):
    pillaCartas = 0
    
    #Mezclar
    random.shuffle(Cartas)
    
    o = 0
    es = ""
    while pillaCartas<17:
        pillaCartas += Cartas[-1]
        o += 1
        if o == 2:
            es = str(pillaCartas)
            vecesCarta[es] += 1

    sumCarta[es] += pillaCartas
    media += pillaCartas/iteraciones

print(media)
print(sumCarta, vecesCarta)
for a, v in sumCarta.items():
    if vecesCarta[a] != 0:
        print(str(sumCarta[a]/vecesCarta[a]))