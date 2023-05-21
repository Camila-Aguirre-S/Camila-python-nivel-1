from baraja import Barajar
from jugador import Jugador


class JuegoBlackjack:
    def __init__(self):
        self.jugador = Jugador()
        self.mazo = Barajar()

    def obtener_carta(self):
        return self.mazo.obtener_carta()

    def pedir_carta_jugador(self, carta):
        self.jugador.pedir_carta(carta)

    def jugar(self):
        # Repartir las cartas iniciales
        for _ in range(2):
            carta_nueva = self.obtener_carta()
            self.pedir_carta_jugador(carta_nueva)
            print("Has obtenido una carta:", carta_nueva)

        while True:
            puntaje_jugador = self.jugador.calcular_puntaje()
            print("Tu puntaje:", puntaje_jugador)

            if puntaje_jugador > 21:
                print("¡Te has pasado de 21! Has perdido.")
                break

            opcion = input("¿Qué acción deseas realizar? (Pedir/Plantarse/Doblar/Rendirse): ")

            if opcion.lower() == "pedir":
                carta_nueva = self.obtener_carta()
                self.pedir_carta_jugador(carta_nueva)
                print("Has obtenido una carta:", carta_nueva)
            elif opcion.lower() == "plantarse":
                break
            elif opcion.lower() == "doblar":
                # Check if doubling down is allowed based on game rules
                if len(self.jugador.mano) == 2:  # Only allowed on the first two cards
                    # Double the wager and draw one more card
                    self.jugador.doblar_apuesta()
                    carta_nueva = self.obtener_carta()
                    self.pedir_carta_jugador(carta_nueva)
                    print("Has obtenido una carta:", carta_nueva)
                    break
                else:
                    print("No puedes doblar en este momento.")
            elif opcion.lower() == "rendirse":
                # Check if surrendering is allowed based on game rules
                if len(self.jugador.mano) == 2:  # Only allowed on the first two cards
                    self.jugador.rendirse()
                    print("Te has rendido. Has perdido la mitad de tu apuesta.")
                    break
                else:
                    print("No puedes rendirte en este momento.")
            else:
                print("Opción inválida. Por favor, elige 'Pedir', 'Plantarse', 'Doblar' o 'Rendirse'.")

        print("Fin del juego")


juego = JuegoBlackjack()
juego.jugar()
