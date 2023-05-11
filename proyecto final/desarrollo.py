#El jugador tiene varias opciones:
#Pedir carta: El jugador puede pedir una carta adicional para aumentar su puntaje. 
             #Puede pedir tantas cartas como desee mientras su puntaje sea inferior a 21.
#Plantarse: El jugador puede decidir no pedir más cartas y quedarse con su puntaje actual.
#Doblar: En algunos casos, el jugador puede optar por doblar su apuesta inicial y recibir una sola carta adicional.
#Dividir: Si las dos primeras cartas del jugador tienen el mismo valor, el jugador puede dividirlas en dos manos separadas 
#y jugar cada una de ellas de forma independiente.

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import random
import usuario
import juego
import desarrollo

lista_cartas = [u'2♠', u'3♠', u'4♠', u'5♠', u'6♠', u'7♠', u'8♠', u'9♠', u'10♠', u'J♠', u'Q♠', u'K♠', u'A♠',
                u'2♥', u'3♥', u'4♥', u'5♥', u'6♥', u'7♥', u'8♥', u'9♥', u'10♥', u'J♥', u'Q♥', u'K♥', u'A♥',
                u'2♦', u'3♦', u'4♦', u'5♦', u'6♦', u'7♦', u'8♦', u'9♦', u'10♦', u'J♦', u'Q♦', u'K♦', u'A♦',
                u'2♣', u'3♣', u'4♣', u'5♣', u'6♣', u'7♣', u'8♣', u'9♣', u'10♣', u'J♣', u'Q♣', u'K♣', u'A♣']

def pedir_carta():
    pedir = random.sample(lista_cartas, 1)
    print(pedir)

def plantarse():
    print("El jugador decide quedarse con sus cartas actuales")

def dividir(cartas_jugador):
    if cartas_jugador[0][-1] == cartas_jugador[1][-1]:
        mano1 = [cartas_jugador[0]]
        mano2 = [cartas_jugador[1]]
        print("Mano 1:", mano1)
        print("Mano 2:", mano2)
        # Puedes continuar el juego para cada mano por separado, realizando operaciones como pedir_carta(), plantarse(), etc.
    else:
        print("No es posible dividir las cartas.")



        