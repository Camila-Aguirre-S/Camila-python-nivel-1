import random
from baraja import Baraja
from jugador import Jugador

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.jugador = None
        self.casa = Jugador("Casa")
        self.estadisticas = {}

    def mostrar_menu_principal(self):
        print("\n--- Menú Principal ---")
        print("1. Registrar usuario")
        print("2. Seleccionar usuario")
        print("3. Iniciar nuevo juego")
        print("4. Mostrar estadísticas")
        print("5. Salir")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del jugador: ")
        self.jugador = Jugador(nombre)
        print(f"\n¡Usuario {nombre} registrado correctamente!")

    def seleccionar_usuario(self):
        if self.jugador is not None:
            print(f"\nUsuario seleccionado: {self.jugador.nombre}")
        else:
            print("\nNo se ha seleccionado ningún usuario.")

    def iniciar_juego(self):
        if self.jugador is None:
            print("No se ha seleccionado ningún usuario. Por favor, seleccione un usuario existente o registre uno nuevo.")
            return

        print(f"\nComienza un nuevo juego.")
        self.baraja.mezclar()

        # Repartir las cartas iniciales
        self.jugador.recibir_carta(self.baraja.repartir_carta())
        self.casa.recibir_carta(self.baraja.repartir_carta())
        self.jugador.recibir_carta(self.baraja.repartir_carta())
        self.casa.recibir_carta(self.baraja.repartir_carta())

        # Mostrar las cartas iniciales del jugador
        print("\nCartas del jugador:")
        self.jugador.mostrar_cartas()

        # Mostrar una carta de la casa y ocultar la otra
        print("\nCartas de la casa:")
        print(f"{self.casa.cartas[0][0]}{self.casa.cartas[0][1]} (Carta oculta)")

        # Verificar si el jugador tiene Blackjack
        if self.jugador.valor_total() == 21:
            print("\n¡Blackjack! ¡Felicidades, has ganado!")
            self.actualizar_estadisticas("ganadas")
            return

        # Continuar jugando
        while True:
            opcion = input("\n¿Qué deseas hacer? (P) Pedir carta, (Q) Quedarse, (S) Salir del juego: ")
            if opcion.upper() == 'P':
                self.jugador.recibir_carta(self.baraja.repartir_carta())
                print("\nCartas del jugador:")
                self.jugador.mostrar_cartas()

                if self.jugador.valor_total() > 21:
                    print("\n¡Te has pasado de 21! ¡Has perdido!")
                    self.actualizar_estadisticas("perdidas")
                    break
            elif opcion.upper() == 'Q':
                # Mostrar la carta oculta de la casa
                print("\nCartas de la casa:")
                self.casa.mostrar_cartas()

                while self.casa.valor_total() < 17:
                    self.casa.recibir_carta(self.baraja.repartir_carta())

                # Mostrar las cartas de la casa una vez que ha terminado de robar
                print("\nCartas de la casa:")
                self.casa.mostrar_cartas()

                if self.casa.valor_total() > 21 or self.jugador.valor_total() > self.casa.valor_total():
                    print("\n¡Felicidades, has ganado!")
                    self.actualizar_estadisticas("ganadas")
                elif self.casa.valor_total() == self.jugador.valor_total():
                    print("\nEmpate. Nadie gana.")
                    self.actualizar_estadisticas("empatadas")
                else:
                    print("\nLa casa gana. Has perdido.")
                    self.actualizar_estadisticas("perdidas")
                break
            elif opcion.upper() == 'S':
                print("\nSaliendo del juego...")
                break
            else:
                print("\nOpción inválida. Inténtalo nuevamente.")

    def mostrar_estadisticas(self):
        print("\n--- Estadísticas ---")
        if self.jugador is not None and self.jugador.nombre in self.estadisticas:
            estadisticas_jugador = self.estadisticas[self.jugador.nombre]
            print(f"Jugador: {self.jugador.nombre}")
            print(f"Partidas ganadas: {estadisticas_jugador['ganadas']}")
            print(f"Partidas perdidas: {estadisticas_jugador['perdidas']}")
            print(f"Partidas empatadas: {estadisticas_jugador['empatadas']}")
        else:
            print("No hay estadísticas disponibles.")

    def actualizar_estadisticas(self, resultado):
        if self.jugador.nombre in self.estadisticas:
            self.estadisticas[self.jugador.nombre][resultado] += 1
        else:
            self.estadisticas[self.jugador.nombre] = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
            self.estadisticas[self.jugador.nombre][resultado] += 1

    def jugar(self):
        print("¡Bienvenido al juego de Blackjack!")

        while True:
            self.mostrar_menu_principal()
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.registrar_usuario()
            elif opcion == '2':
                self.seleccionar_usuario()
            elif opcion == '3':
                self.iniciar_juego()
            elif opcion == '4':
                self.mostrar_estadisticas()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("\nOpción inválida. Inténtalo nuevamente.")


juego = Juego()
juego.jugar()
