from estadisticas import guardar_estadisticas, cargar_estadisticas
from jugador import Jugador
from baraja import Baraja
import random

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.jugador = None
        self.casa = Jugador("Casa")
        self.estadisticas = []

    def jugar(self):
        """
        Función principal para iniciar el juego.
        """
        print("¡Bienvenido al juego de Blackjack!")
        while True:
            print("\n--- Menú Principal ---")
            print("1. Seleccionar usuario")
            print("2. Iniciar nuevo juego")
            print("3. Mostrar estadísticas")
            print("4. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                self.seleccionar_usuario()
            elif opcion == '2':
                self.iniciar_juego()
            elif opcion == '3':
                self.mostrar_estadisticas()
            elif opcion == '4':
                print("Gracias por jugar. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Inténtalo nuevamente.")

    def seleccionar_usuario(self):
        """
        Función para seleccionar el nombre del jugador.
        """
        nombre = input("Ingrese el nombre del jugador: ")
        self.jugador = Jugador(nombre)
        print(f"\n¡Bienvenido, {nombre}!")

    def iniciar_juego(self):
        """
        Función para iniciar un nuevo juego.
        """
        print("\nComienza un nuevo juego.")

        # Mezclar la baraja antes de iniciar el juego
        self.baraja.mezclar()

        # Reiniciar las cartas del jugador y la casa
        self.jugador.cartas = []
        self.casa.cartas = []

        # Repartir dos cartas al jugador y una carta a la casa
        for _ in range(2):
            carta = self.baraja.repartir_carta()
            self.jugador.recibir_carta(carta)

        carta_casa = self.baraja.repartir_carta()
        self.casa.recibir_carta(carta_casa)

        # Mostrar estado del juego
        self.mostrar_estado_juego()

        # Menú de juego
        while True:
            print("\n--- Menú de Juego ---")
            print("1. Pedir carta")
            print("2. Plantarse")
            print("3. Mostrar estado del juego")

            opcion = input("Ingrese el número de la acción deseada: ")

            if opcion == '1':
                self.pedir_carta()
            elif opcion == '2':
                self.plantarse()
                break
            elif opcion == '3':
                self.mostrar_estado_juego()
            else:
                print("Opción inválida. Inténtalo nuevamente.")

    def pedir_carta(self):
        """
        Función para que el jugador pida una carta adicional.
        """
        carta = self.baraja.repartir_carta()
        self.jugador.recibir_carta(carta)
        self.mostrar_estado_juego()

        valor_total = self.jugador.valor_total()
        if valor_total == 777:
            print("\n¡Tres sietes! ¡Ganaste!")
            self.guardar_estadisticas("Ganado")
            self.jugar_otra_partida()
        elif valor_total == 555:
            print("\n¡Cinco menores! ¡Ganaste!")
            self.guardar_estadisticas("Ganado")
            self.jugar_otra_partida()
        elif valor_total == 21:
            print("\n¡Blackjack! ¡Ganaste!")
            self.guardar_estadisticas("Ganado")
            self.jugar_otra_partida()
        elif valor_total > 21:
            print("\n¡Te pasaste de 21! Has perdido.")
            self.guardar_estadisticas("Perdido")
            self.jugar_otra_partida()

    def plantarse(self):
        """
        Función para que el jugador se plante y jugar la ronda de la casa.
        """
        valor_jugador = self.jugador.valor_total()
        print(f"\nTe has plantado con un valor total de {valor_jugador}.")

        # Jugar la ronda de la casa
        while True:
            valor_casa = self.jugar_ronda_casa()
            print(f"Valor total de la casa: {valor_casa}\n")

            if valor_casa > 21:
                print("La casa se pasó de 21. ¡Ganaste!")
                self.guardar_estadisticas("Ganado")
                break
            elif valor_casa > valor_jugador:
                print("La casa tiene un valor mayor. Has perdido.")
                self.guardar_estadisticas("Perdido")
                break
            elif valor_casa < valor_jugador:
                print("Tu valor es mayor. ¡Has ganado!")
                self.guardar_estadisticas("Ganado")
                break
            else:
                print("Empate")
                self.guardar_estadisticas("Empate")
                break

        self.jugar_otra_partida()

    def jugar_ronda_casa(self):
        """
        Función para jugar la ronda de la casa.
        """
        while True:
            valor_casa = self.casa.valor_total()

            # Cuando la casa se planta si tiene un valor igual o mayor a 17
            if valor_casa >= 17:
                break

            # Si la casa pide una carta adicional si tiene un valor menor a 17
            carta = self.baraja.repartir_carta()
            self.casa.recibir_carta(carta)

        return valor_casa

    def mostrar_estado_juego(self):
        """
        Función para mostrar estado actual del juego.
        """
        print("\n--- Estado del Juego ---")
        print(f"Jugador: {self.jugador.nombre}")
        print("Cartas del jugador:")
        self.jugador.mostrar_cartas()
        print(f"Valor total del jugador: {self.jugador.valor_total()}")

        print("\nCartas de la casa:")
        print(f"{self.casa.cartas[0][0]}{self.casa.cartas[0][1]}")  # Muestra solo la primera carta de la casa

    def guardar_estadisticas(self, resultado):
        """
        Función para guardar las estadísticas de la partida.
        """
        self.estadisticas.append(resultado)

        # Si ya se han jugado 5 partidas, eliminar la más antigua
        if len(self.estadisticas) > 5:
            self.estadisticas.pop(0)

    def mostrar_estadisticas(self):
        """
        Función para mostrar las estadísticas de las últimas partidas.
        """
        print("\n--- Estadísticas ---")
        if len(self.estadisticas) == 0:
            print("No se han jugado partidas aún.")
        else:
            print("Últimas 5 partidas:")
            for partida in self.estadisticas:
                print(partida)

    def jugar_otra_partida(self):
        """
        Función para preguntar si se desea jugar otra partida.
        """
        while True:
            opcion = input("\n¿Deseas jugar otra partida? (s/n): ")
            if opcion.lower() == 's':
                self.iniciar_juego()
                break
            elif opcion.lower() == 'n':
                print("¡Gracias por jugar!")
                self.jugador = None
                break
            else:
                print("Opción inválida. Inténtalo nuevamente.")


# Código de ejecución del juego
juego = Juego()
juego.jugar()
