from mano import Mano

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
