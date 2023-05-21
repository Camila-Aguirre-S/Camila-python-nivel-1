from jugador import Jugador
from dealer import Dealer
from baraja import Baraja
from mano import Manos



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

            self.dealer.jugar(self.baraja)

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
            elif accion == "P":
                jugador.jugando = False
            else:
                print("Acción inválida. Por favor, elige P o P.")

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
