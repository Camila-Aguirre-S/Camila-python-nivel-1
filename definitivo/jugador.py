class Jugador:
    def __init__(self):
        self.mano = []
    
    def pedir_carta(self, carta):
        self.mano.append(carta)
    
    def calcular_puntaje(self):
        puntaje = 0
        for carta in self.mano:
            if carta[-1] == 'A':
                puntaje += 11
            elif carta[:-1] in ['K', 'Q', 'J']:
                puntaje += 10
            else:
                puntaje += int(carta[:-1])
        return puntaje
