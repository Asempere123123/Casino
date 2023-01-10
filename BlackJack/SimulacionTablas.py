import random

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

for _ in range(iteraciones):
    Cartas = []
    Croupier = []

    if len(Deck) <= 5:
        newDeck(Deck)

    twoCards(Cartas)
    twoCards(Croupier)
    
    print(Cartas, Croupier)