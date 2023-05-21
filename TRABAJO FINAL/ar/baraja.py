import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []
        for palo in ["Picas", "Corazones", "Tréboles", "Diamantes"]:
            for valor in range(2, 11):
                carta = Carta(valor, palo)
                self.cartas.append(carta)
            for valor in ["J", "Q", "K", "A"]:
                carta = Carta(valor, palo)
                self.cartas.append(carta)

    def mezclar(self):
        random.shuffle(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) == 0:
            return None
        else:
            return self.cartas.pop()

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)
