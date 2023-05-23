class Jugador:
    def __init__(self, nombre):
        # Inicializar el jugador con su nombre y una lista vacía de cartas
        self.nombre = nombre
        self.cartas = []

    def recibir_carta(self, carta):
        # Añadir una carta recibida al jugador
        self.cartas.append(carta)

    def mostrar_cartas(self):
        # Mostrar las cartas del jugador
        for carta in self.cartas:
            print(f"{carta[0]}{carta[1]}")

    def valor_total(self):
        # Calcular el valor total de las cartas del jugador
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total = sum(valores[carta[0]] for carta in self.cartas)

        # Ajustar el valor del As si se supera 21
        ases = sum(1 for carta in self.cartas if carta[0] == 'A')
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1

        return total
