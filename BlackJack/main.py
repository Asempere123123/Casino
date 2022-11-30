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

    privatecard = 0

cards = []
mesacards = []
mesapcard = int()

Cartas = []

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
            print(player.privatecard, cards[player.id], str(CantidadCartas(cards[player.id], player.privatecard)))
            msg = "want a card?"
            a = input("%s (y/n/s) " % msg).lower()
            if a == "y":
                cards[player.id].append(Cartas[-1])
                del Cartas[-1]
                if (CantidadCartas(cards[player.id], player.privatecard))>21:
                    print("bro as perdio eres to nup")
                    exit = False
            elif a == "s":
                numPlayers += 1
                Players.append(Player(numPlayers)) #no se si es -1
                print(Players[numPlayers-1].id, len(Players))
                

                

            else:
                print(CantidadCartas(cards[player.id], player.privatecard))
                exit = False
            

#la mano
while (CantidadCartas(mesacards, mesapcard))<17:
    mesacards.append(Cartas[-1])
    del Cartas[-1]
print(mesacards, mesapcard, CantidadCartas(mesacards, mesapcard))