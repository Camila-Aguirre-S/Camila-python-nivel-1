import json

def guardar_estadisticas(estadisticas):
    with open("estadisticas.txt", "w") as archivo:
        for nombre, resultados in estadisticas.items():
            archivo.write(f"{nombre}: {' - '.join(resultados)}\n")

def cargar_estadisticas():
    try:
        with open("estadisticas.txt", "r") as archivo:
            estadisticas = {}
            for linea in archivo:
                nombre, resultados_str = linea.strip().split(":")
                resultados = resultados_str.split(" - ")
                estadisticas[nombre] = resultados
            return estadisticas
    except FileNotFoundError:
        return {}
