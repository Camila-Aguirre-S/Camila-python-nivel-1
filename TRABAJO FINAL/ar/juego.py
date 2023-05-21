import random
from jugador import Jugador
from casa import Casa

class Juego:
    def __init__(self, nombre_usuario):
        self.jugador = Jugador(nombre_usuario)
        self.casa = Casa()

    def iniciar_juego(self):
        print("Bienvenido(a) al juego de Blackjack!")
        print(f"Comenzando juego con el jugador: {self.jugador.nombre}\n")

        while True:
            self.jugador.nueva_partida()
            self.casa.nueva_partida()

            self.repartir_cartas_iniciales()
            self.mostrar_estado_juego()

            if self.jugador.tiene_blackjack() or self.casa.tiene_blackjack():
                self.mostrar_resultados()
            else:
                self.jugar_turno_jugador()
                self.jugar_turno_casa()
                self.mostrar_resultados()

            if not self.nuevo_juego():
                break

    def repartir_cartas_iniciales(self):
        self.jugador.recibir_carta(self.barajar_carta())
        self.casa.recibir_carta(self.barajar_carta())
        self.jugador.recibir_carta(self.barajar_carta())
        self.casa.recibir_carta(self.barajar_carta(escondida=True))

    def jugar_turno_jugador(self):
        while self.jugador.en_juego:
            accion = input("¿Qué deseas hacer? (p)edir carta o (p)lantarte: ").lower()
            if accion == "p":
                self.jugador.recibir_carta(self.barajar_carta())
                self.mostrar_estado_juego()
                if self.jugador.tiene_mano_superior_a_21():
                    self.jugador.perder()
                    break
            else:
                self.jugador.plantarse()
                break

    def jugar_turno_casa(self):
        self.casa.revelar_carta_escondida()
        self.mostrar_estado_juego()

        while self.casa.debe_pedir_carta():
            self.casa.recibir_carta(self.barajar_carta())
            self.mostrar_estado_juego()
            if self.casa.tiene_mano_superior_a_21():
                self.casa.perder()
                break

    def mostrar_estado_juego(self):
        print("\n--- Estado del Juego ---")
        self.casa.mostrar_mano()
        self.jugador.mostrar_mano()
        self.jugador.mostrar_estado()
        print("------------------------\n")

    def mostrar_resultados(self):
        print("\n--- Resultados ---")
        self.casa.revelar_cartas()
        self.casa.mostrar_mano()
        self.jugador.mostrar_mano()
        self.jugador.mostrar_resultado()
        print("------------------\n")

    def barajar_carta(self, escondida=False):
        palos = ["♠", "♥", "♦", "♣"]
        numeros = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        carta = random.choice(numeros) + random.choice(palos)
        if escondida:
            return f"?{carta[1]}"
        return carta

    def nuevo_juego(self):
        respuesta = input("¿Deseas jugar otra partida? (s)i/(n)o: ").lower()
        return respuesta == "s"

