class Score:

    def __init__(self, puntos):
        self.puntos = puntos

    def anotacion(self, cantidad):
        self.puntos += cantidad

    def ganarset(self, score1):
        if (score1.puntos >= 40):
            self.puntos = "Set ganado"