from valores import valores

def calcular_puntaje(cartas_jugador):
    puntaje = 0
    for carta in cartas_jugador:
        valor = valores[carta[:-1]]  # Obtener el valor de la carta del diccionario de valores
        puntaje += valor
    return puntaje
