import random
import csv

#Zona output

#end zona output

with open('bj7.csv', newline='') as f:
    reader = csv.reader(f)
    tabla = list(reader)

iteraciones = 100

Deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random.shuffle(Deck)

def newDeck(deck):
    deck += [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    random.shuffle(deck)

def twoCards(quien):
    l = Deck[-2:]
    del Deck[-2:]
    quien += l

def coger(quien):
    l = Deck[-1]
    del Deck[-1]
    quien.append(l)

def sumCartas(ls):
    asamount = 0
    count = 0
    
    for i in ls:
        if i == 1:
            count += 11
            asamount +=1
        else:
            count += i
    
    while count > 21 and asamount > 0:
        count -= 10
        asamount -= 1

    return count

for _ in range(iteraciones):
    Cartas = []
    Croupier = []

    if len(Deck) <= 5:
        newDeck(Deck)

    twoCards(Cartas)
    twoCards(Croupier)

    
    while True:
        sum = sumCartas(Cartas)

        if sum > 21:
            break

        print(sum, Croupier[0])
        if sum <=11:
            sum = 11

        print(tabla[sum-10][Croupier[0]-1], "sum: " + str(sum), "Croupier: " + str(Croupier[0]))
        if tabla[sum-10][Croupier[0]-1] == "P":
            coger(Cartas)

        else:
            break

    while sumCartas(Croupier) < 17:
        coger(Croupier)
    
    if sumCartas(Cartas) <= 21:
        if sumCartas(Cartas) > sumCartas(Croupier):
            #ganas
            pass
        elif sumCartas(Cartas) == sumCartas(Croupier):
            #empate
            pass
        else:
            #pierdes
            pass
    else:
        #pierdes
        pass