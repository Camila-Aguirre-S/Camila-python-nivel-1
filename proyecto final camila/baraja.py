import random 
class Baraja:
    def __init__(self):
        # Inicializar los palos y valores de la baraja
        self.palos = ['♠', '♣', '♥', '♦']
        self.valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartas = []

        # Crear todas las combinaciones de palo y valor para formar las cartas
        for palo in self.palos:
            for valor in self.valores:
                self.cartas.append((valor, palo))

    def mezclar(self):
        # Mezclar las cartas de la baraja
        random.shuffle(self.cartas)

    def repartir_carta(self):
        # Repartir una carta de la baraja
        return self.cartas.pop()

    def __len__(self):
        # Obtener la cantidad de cartas restantes en la baraja
        return len(self.cartas)
