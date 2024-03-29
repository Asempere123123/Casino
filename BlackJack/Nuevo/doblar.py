import csv, random

with open('TablaDoblar.csv', newline='') as f:
    reader = csv.reader(f)
    tabla = list(reader)

def chooseAction(m, cr):
    return tabla[m][cr]

apuestaInicial = 1
iteraciones = 1000000
dinero = 0

bet = apuestaInicial
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

for _ in range(0, iteraciones):

    bet = apuestaInicial
    Cartas = []
    Croupier = []

    if len(Deck) <= 15:
        newDeck(Deck)

    twoCards(Cartas)
    twoCards(Croupier)
    c = sumCartas(Cartas)
    cr = Croupier[0]
    
    haspedido = False
    while True:
        sum = sumCartas(Cartas)
        ff = False

        if sum > 21:
            break
        
        accion = chooseAction(c, cr)

        
        if accion == "P":
            coger(Cartas)
            haspedido = True

        elif accion == "D":
            if not haspedido:
                bet *= 2
                haspedido = True
            coger(Cartas)
        elif accion == "Rp":
            dinero -= bet/2
            ff = True  
            break
            
        else:
            break

    while sumCartas(Croupier) < 17:
        coger(Croupier)

    sumc = 0
    summ = 0
    if sumCartas(Cartas) > 22:
        sumc = 22
    else:
        sumc = sumCartas(Cartas)
    if sumCartas(Croupier) > 22:
        summ = 22
    else:
        summ = sumCartas(Croupier)

    if not ff:
        if sumc <= 21:

            if summ <= 21:
                if sumc > summ:
                    #ganas
                    dinero += bet

                    if sumc == 21 and len(Cartas) == 2:
                        dinero += bet/2

                elif sumc == summ:
                    #empate

                    dinero += bet

                    if sumc == 21 and len(Cartas) == 2:
                        dinero += bet/2
                else:
                    #pierdes
                    dinero -= bet
            else:
                #ganas
                dinero += bet

                if sumc == 21 and len(Cartas) == 2:
                        dinero += bet/2
        else:
            #pierdes
            dinero -= bet

#output
print(dinero)