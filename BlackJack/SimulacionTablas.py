import random
import csv

#Zona output
dinero = 0
apuestainicial = 10
apuesta = apuestainicial
#end zona output

with open('bi.csv', newline='') as f:
    reader = csv.reader(f)
    tabla = list(reader)

iteraciones = 10000

Deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random.shuffle(Deck)

def newDeck(deck):
    new = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(new)

    deck += new

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
        if i == 11:
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

    apuesta = apuestainicial

    if len(Deck) <= 15:
        newDeck(Deck)

    twoCards(Cartas)
    twoCards(Croupier)
    
    haspedido = False
    while True:
        sum = sumCartas(Cartas)

        if sum > 21:
            break
        
         

        accion = tabla[sum-3][Croupier[0]-1]

        if accion == "P":
            coger(Cartas)
            haspedido = True

        elif accion == "D":
            if haspedido == True:
                break
            apuesta = 2*apuestainicial

            coger(Cartas)
            break
        elif accion == "R":
            if haspedido == True:
                break
            sum = 22

            dinero += apuesta/2
            break
        else:
            break

    while sumCartas(Croupier) < 17:
        coger(Croupier)

    if sumCartas(Cartas) <= 21:

        if sumCartas(Croupier) <= 21:
            if sumCartas(Cartas) > sumCartas(Croupier):
                #ganas
                dinero += apuesta
        
            elif sumCartas(Cartas) == sumCartas(Croupier):
                #empate
                pass
            else:
                #pierdes
                dinero -= apuesta
        else:
            #ganas
            dinero += apuesta
    else:
        #pierdes
        dinero -= apuesta

#output
print(dinero)