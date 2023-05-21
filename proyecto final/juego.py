import random


class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.puntuacion = self._calcular_puntuacion()

    def __str__(self):
        return f"{self.valor} de {self.palo}"

    def _calcular_puntuacion(self):
        if self.valor in ["Jota", "Reina", "Rey"]:
            return 10
        elif self.valor == "As":
            return 11
        else:
            return int(self.valor)


class Baraja:
    def __init__(self):
        self.cartas = []
        self._crear_baraja()

    def _crear_baraja(self):
        palos = ["Espadas", "Corazones", "Diamantes", "Tréboles"]
        valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jota", "Reina", "Rey", "As"]
        self.cartas = [Carta(palo, valor) for palo in palos for valor in valores]
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def obtener_valor(self):
        valor = sum(carta.puntuacion for carta in self.cartas)
        num_ases = sum(carta.valor == "As" for carta in self.cartas)
        while valor > 21 and num_ases > 0:
            valor -= 10
            num_ases -= 1
        return valor


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()
        self.jugando = True
        self.ganador = False

    def agregar_carta_a_mano(self, carta):
        self.mano.agregar_carta(carta)

    def obtener_valor_mano(self):
        return self.mano.obtener_valor()

    def establecer_ganador(self):
        self.ganador = True


class Dealer(Jugador):
    def __init__(self):
        super().__init__("Dealer")
        self.mostrar_todas_las_cartas = False

    def jugar(self):
        while self.obtener_valor_mano() < 17:
            self.agregar_carta_a_mano(baraja.repartir_carta())

        self.mostrar_todas_las_cartas = True


class JuegoBlackjack:
    def __init__(self):
        self.jugadores = []
        self.baraja = Baraja()
        self.dealer = Dealer()

    def iniciar(self):
        self.imprimir_mensaje_bienvenida()
        self.crear_jugador()
        self.jugar_partida()

    def imprimir_mensaje_bienvenida(self):
        print("¡Bienvenido a Blackjack!")

    def crear_jugador(self):
        nombre = input("Ingresa tu nombre: ")
        jugador = Jugador(nombre)
        self.jugadores.append(jugador)

    def jugar_partida(self):
        while True:
            self.repartir_cartas_iniciales()
            self.mostrar_estado_juego()

            for jugador in self.jugadores:
                self.jugar_turno_jugador(jugador)

            self.dealer.jugar()

            self.determinar_ganadores()

            self.mostrar_resultados()

            if not self.jugar_de_nuevo():
                break

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            for jugador in self.jugadores:
                jugador.agregar_carta_a_mano(self.baraja.repartir_carta())
            self.dealer.agregar_carta_a_mano(self.baraja.repartir_carta())

    def mostrar_estado_juego(self):
        print("\n--- Estado del Juego ---")
        print("Mano del Dealer:")
        for carta in self.dealer.mano.cartas:
            if self.dealer.mostrar_todas_las_cartas:
                print(carta)
            else:
                print("Carta oculta")
                break

        print("\nMano de los Jugadores:")
        for jugador in self.jugadores:
            print(f"{jugador.nombre}:")
            for carta in jugador.mano.cartas:
                print(carta)
            print(f"Puntuación total: {jugador.obtener_valor_mano()}")
            print()

    def jugar_turno_jugador(self, jugador):
        while jugador.jugando:
            accion = input(f"{jugador.nombre}, ¿quieres (P)edir carta o (P)arar? ").upper()
            if accion == "P":
                jugador.agregar_carta_a_mano(self.baraja.repartir_carta())
                self.mostrar_estado_juego()
                if jugador.obtener_valor_mano() > 21:
                    print(f"{jugador.nombre} se pasó de 21. ¡Perdiste!")
                    jugador.jugando = False
            elif accion == "A":
                jugador.jugando = False
            else:
                print("Acción inválida. Por favor, elige P o A.")

    def determinar_ganadores(self):
        valor_mano_dealer = self.dealer.obtener_valor_mano()
        for jugador in self.jugadores:
            valor_mano_jugador = jugador.obtener_valor_mano()
            if valor_mano_jugador > 21:
                jugador.ganador = False
            elif valor_mano_dealer > 21:
                jugador.establecer_ganador()
            elif valor_mano_jugador > valor_mano_dealer:
                jugador.establecer_ganador()
            elif valor_mano_jugador == valor_mano_dealer:
                jugador.ganador = False
            else:
                jugador.ganador = False

    def mostrar_resultados(self):
        print("\n--- Resultados ---")
        for jugador in self.jugadores:
            if jugador.ganador:
                print(f"{jugador.nombre} ha ganado!")
            else:
                print(f"{jugador.nombre} ha perdido.")

    def jugar_de_nuevo(self):
        respuesta = input("¿Quieres jugar de nuevo? (S/N) ").upper()
        return respuesta == "S"


juego = JuegoBlackjack()
juego.iniciar()

