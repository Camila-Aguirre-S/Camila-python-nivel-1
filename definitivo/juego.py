from baraja import Barajar
from jugador import Jugador
import random
from  class blackjack import def jugar


class Juego:
    def __init__(self):
        self.baraja = Barajar()
        self.usuarios = []
        self.blackjack_game = None

    def iniciar_juego(self):
        while True:
            print("Opciones:")
            print("1. Nuevo usuario")
            print("2. Nuevo juego")
            print("3. Estadísticas")
            print("4. Salir")
            seleccion = input("Seleccione una opción (1, 2, 3, 4): ")

            try:
                seleccion = int(seleccion)
                if seleccion == 1:
                    self.nuevo_usuario()
                elif seleccion == 2:
                    self.nuevo_juego()
                elif seleccion == 3:
                    self.estadisticas()
                elif seleccion == 4:
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def nuevo_usuario(self):
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        self.usuarios.append(nombre)
        print("Usuario", nombre, "agregado correctamente.")

    def nuevo_juego(self):
        self.baraja.barajar()
        self.baraja.repartir_carta_casa()

        cartas_jugador = self.baraja.obtener_cartas_jugador()
        cartas_casa = self.baraja.obtener_cartas_casa()

        print("Mano de la casa:", cartas_casa)
        print("Mano del jugador:", cartas_jugador)

        self.blackjack_game = BlackjackGame(self.baraja)
        self.blackjack_game.iniciar_juego(cartas_jugador, cartas_casa)

        print("Estado del juego:", self.blackjack_game.obtener_estado_juego())
        jugar ()
    def estadisticas(self):
        for usuario in self.usuarios:
            print("Estadísticas para el usuario:", usuario)
            # Aquí puedes implementar la lógica para mostrar las estadísticas del usuario
            # utilizando los datos almacenados en los archivos de texto


juego = JuegoBlackjack()
juego.jugar()
