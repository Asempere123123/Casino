class Baraja:
    def __init__(self):
        self.crear_baraja()
        self.cartas_usadas = []

    def crear_baraja(self):
        self.cartas = []
        palos = ["espadas", "corazones", "diamantes", "tréboles"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for palo in palos:
            for valor in valores:
                carta = {"palo": palo, "valor": valor}
                self.cartas.append(carta)
                
    def jugar_partida(self):
        while len(self.cartas)>0:
            #juego
            pass
        self.cartas.extend(self.cartas_usadas)
        self.cartas_usadas.clear()
        self.mezclar()