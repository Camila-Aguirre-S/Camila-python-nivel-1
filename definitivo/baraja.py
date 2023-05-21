import random

class Barajar:
    def __init__(self):
        self.lista_cartas = [
            u'2♠', u'3♠', u'4♠', u'5♠', u'6♠', u'7♠', u'8♠', u'9♠', u'10♠', u'J♠', u'Q♠', u'K♠', u'A♠',
            u'2♥', u'3♥', u'4♥', u'5♥', u'6♥', u'7♥', u'8♥', u'9♥', u'10♥', u'J♥', u'Q♥', u'K♥', u'A♥',
            u'2♦', u'3♦', u'4♦', u'5♦', u'6♦', u'7♦', u'8♦', u'9♦', u'10♦', u'J♦', u'Q♦', u'K♦', u'A♦',
            u'2♣', u'3♣', u'4♣', u'5♣', u'6♣', u'7♣', u'8♣', u'9♣', u'10♣', u'J♣', u'Q♣', u'K♣', u'A♣'
        ]
        self.cartas_jugador = []
        self.cartas_casa = []

    def barajar(self):
        random.shuffle(self.lista_cartas)
        self.cartas_jugador = random.sample(self.lista_cartas, 2)

    def repartir_carta_casa(self):
        self.cartas_casa = random.sample(self.lista_cartas, 1)

    def obtener_cartas_jugador(self):
        return self.cartas_jugador

    def obtener_cartas_casa(self):
        return self.cartas_casa
