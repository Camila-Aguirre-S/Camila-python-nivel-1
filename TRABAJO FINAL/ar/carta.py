class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        palo_unicode = {
            "Picas": "\u2660",
            "Corazones": "\u2665",
            "Tréboles": "\u2663",
            "Diamantes": "\u2666"
        }
        return f"{self.valor} {palo_unicode[self.palo]}"
