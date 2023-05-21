import random


lista_cartas = [u'2♠', u'3♠', u'4♠', u'5♠', u'6♠', u'7♠', u'8♠', u'9♠', u'10♠', u'J♠', u'Q♠', u'K♠', u'A♠',
                u'2♥', u'3♥', u'4♥', u'5♥', u'6♥', u'7♥', u'8♥', u'9♥', u'10♥', u'J♥', u'Q♥', u'K♥', u'A♥',
                u'2♦', u'3♦', u'4♦', u'5♦', u'6♦', u'7♦', u'8♦', u'9♦', u'10♦', u'J♦', u'Q♦', u'K♦', u'A♦',
                u'2♣', u'3♣', u'4♣', u'5♣', u'6♣', u'7♣', u'8♣', u'9♣', u'10♣', u'J♣', u'Q♣', u'K♣', u'A♣']

def barajar_cartas():
        random.shuffle(lista_cartas)
        cartas_jugador1= random.sample(lista_cartas, 2)
        print(cartas_jugador1)   
        pass


def cartacasa():
        cartas_casa = random.sample(lista_cartas, 1)
        print(cartas_casa)