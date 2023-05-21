from mano import Mano

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()

    def recibir_carta(self, carta):
        self.mano.agregar_carta(carta)

    def calcular_puntaje(self):
        return self.mano.obtener_valor()

    def __str__(self):
        return f"Mano del jugador {self.nombre}: {str(self.mano)}"
