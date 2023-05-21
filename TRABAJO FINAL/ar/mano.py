from carta import Carta

def class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def obtener_valor(self):
        valor = 0
        ases = 0
        for carta in self.cartas:
            if carta.valor in ["J", "Q", "K"]:
                valor += 10
            elif carta.valor == "A":
                valor += 11
                ases += 1
            else:
                valor += carta.valor
        while valor > 21 and ases > 0:
            valor -= 10
            ases -= 1
        return valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)
