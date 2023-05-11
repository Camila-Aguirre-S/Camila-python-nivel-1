# -*- coding: utf-8 -*-

import random
import usuario
import juego
import desarrollo

lista_cartas = [u'2♠', u'3♠', u'4♠', u'5♠', u'6♠', u'7♠', u'8♠', u'9♠', u'10♠', u'J♠', u'Q♠', u'K♠', u'A♠',
                u'2♥', u'3♥', u'4♥', u'5♥', u'6♥', u'7♥', u'8♥', u'9♥', u'10♥', u'J♥', u'Q♥', u'K♥', u'A♥',
                u'2♦', u'3♦', u'4♦', u'5♦', u'6♦', u'7♦', u'8♦', u'9♦', u'10♦', u'J♦', u'Q♦', u'K♦', u'A♦',
                u'2♣', u'3♣', u'4♣', u'5♣', u'6♣', u'7♣', u'8♣', u'9♣', u'10♣', u'J♣', u'Q♣', u'K♣', u'A♣']

opciones = {
    '1': usuario.crear_usuario,
    '2': juego.nuevo_juego,
    '3': juego.mostrar_estadisticas,
    '4': juego.salir
}

while True:
    print("Opciones:")
    print("1. Nuevo usuario")
    print("2. Nuevo juego")
    print("3. Estadísticas")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1, 2, 3, 4): ")

    if seleccion in opciones:
        if seleccion == '1':
            opciones[seleccion]()
        elif seleccion == '2' or seleccion == '3':
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            opciones[seleccion](nombre_usuario)
        else:
            opciones[seleccion]()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    if seleccion == '2':
        random.shuffle(lista_cartas)
        cartas_jugador = random.sample(lista_cartas, 2)
        print(cartas_jugador)
        cartas_casa = random.sample(lista_cartas, 1)
        print(cartas_casa)


    opciones_juego = {
    'a': desarrollo.pedir_carta,
    'b': desarrollo.plantarse,
    'c': desarrollo.dividir,
    }

    while True:
        print("Opciones de juego:")
        print("a. Pedir carta")
        print("b. Plantarse")
        print("c. Dividir")
        seleccion_juego = input("Seleccione una opción (a, b, c): ")

        if seleccion_juego in opciones_juego:
            if seleccion_juego == 'a':
                opciones_juego[seleccion_juego]()
            elif seleccion_juego == 'b':
                opciones_juego[seleccion_juego]()
            elif seleccion_juego == 'c':
                opciones_juego[seleccion_juego](cartas_jugador)
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
       

