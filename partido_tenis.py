class Score:

    def __init__(self, puntos):
        self.puntos = puntos

    def anotacion(self, score1):
        if (score1.puntos >= 0) and (score1.puntos <= 29):
            self.puntos += 15

    def ganarset(self, score1):
        if (score1.puntos >= 40):
            self.puntos = "Set ganado"