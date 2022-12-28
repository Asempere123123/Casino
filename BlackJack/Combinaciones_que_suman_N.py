#ni cerca de funcional

n = 10
profundidad = 6

Cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

for i in range(profundidad):
    cartas = []

    for j in range(i):
        cartas.append(Cartas[-1])
        del Cartas[-1]