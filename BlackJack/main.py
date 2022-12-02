import random

def CantidadCartas(ls, c):
    asamount = 0
    count = 0

    if c == 1:
        count += 11
        asamount += 1
    else:
        count += c

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

class Player:
    def __init__(self, id):
        self.id = id

    owner = None
    apuesta = 0
    privatecard = 0

cards = []
mesacards = []
mesapcard = int()

Cartas = []

startingMoney = 1000
apuestaInicial = 10
money = []
#lomismo hands = []

for i in range(0, 61):
    if i < 4:
        Cartas.append(1)
    if 4 < i < 9:
        Cartas.append(2)
    if 9 < i < 14:
        Cartas.append(3)
    if 14 < i < 19:
        Cartas.append(4)
    if 19 < i < 24:
        Cartas.append(5)
    if 24 < i < 29:
        Cartas.append(6)
    if 29 < i < 34:
        Cartas.append(7)
    if 34 < i < 39:
        Cartas.append(8)
    if 39 < i < 44:
        Cartas.append(9)
    if 44 < i:
        Cartas.append(10)
#Mezclar
random.shuffle(Cartas)
print(Cartas)
#Repartir
numPlayers = 2 #Cantidad de jugadores total
Players = []

for playerID in range(0, numPlayers):
    Players.append(Player(playerID))

for player in Players:
    player.privatecard = Cartas[-1]
    del Cartas[-1]
    cards.append([Cartas[-1]])
    del Cartas[-1]

    player.owner = player.id
    money.append(startingMoney)
    player.apuesta = apuestaInicial
    #añadir sistema posesion hands.append([player.id])

mesacards.append(Cartas[-1])
del Cartas[-1]
mesapcard = Cartas[-1]
del Cartas[-1]
print(Cartas, mesacards, mesapcard)

#Gameplay
automatic = False #select if using a bot

def botOutput():
    return False


for player in Players:
    if automatic:
        exit = True
        while exit:
            if botOutput:
                cards[player.id].append(Cartas[-1])
                del Cartas[-1]
            else:
                exit = False
    
    else:
        exit = True
        while exit:
            print(player.privatecard, cards[player.id], str(CantidadCartas(cards[player.id], player.privatecard)), "owner:", player.owner)
            msg = "want a card?"
            a = input("%s (y/n/s) " % msg).lower()
            if a == "y":
                cards[player.id].append(Cartas[-1])
                del Cartas[-1]
                if (CantidadCartas(cards[player.id], player.privatecard))>21:
                    print("bro as perdio eres to nup")
                    exit = False
            elif a == "s":
                
                if player.privatecard in cards[player.id]:

                    numPlayers += 1
                    Players.insert(player.id+1, Player(numPlayers-1)) #no se si es +1
                    cards.append(cards[player.id])
                
                    Players[player.id+1].privatecard = Cartas[-1]
                    del Cartas[-1]
                    cards[player.id] = [Cartas[-1]]
                    del Cartas[-1]
                    Players[player.id+1].apuesta = player.apuesta
                
                    print("1:", player.privatecard, cards[player.id], "2:", Players[player.id+1].privatecard, cards[numPlayers-1], cards[Players[numPlayers-1].id])
                    Players[player.id+1].owner = player.owner #lo mismo hands[player.id].append()
                else:
                    print("No puedes splitear")
                
            else:
                print(CantidadCartas(cards[player.id], player.privatecard))
                exit = False
            

#la mano
while (CantidadCartas(mesacards, mesapcard))<17:
    mesacards.append(Cartas[-1])
    del Cartas[-1]
print(mesacards, mesapcard, CantidadCartas(mesacards, mesapcard))

#cuenta beneficios
cm = CantidadCartas(mesacards, mesapcard)

for player in Players:
    c = CantidadCartas(cards[player.id], player.privatecard)
    if c == 21 and cm != 21:
        money[player.owner] += int(player.apuesta*1.5)
    elif c < 21 and c > cm:
        money[player.owner] += player.apuesta
    elif c < cm and c < 21:
        money[player.owner] -= player.apuesta
    elif cm > 21 and c <= 21:
        money[player.owner] += player.apuesta
    elif c > 21:
        money[player.owner] -= player.apuesta

print(money)