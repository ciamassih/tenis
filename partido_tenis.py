class Score:

    def __init__(self, puntos):
        self.puntos = puntos

    def anotacion(self, score):
        if (score.puntos >= 0) and (score.puntos <= 29):
            self.puntos += 15
        elif (score.puntos == 30):
            self.puntos += 10
        elif (score.puntos == 40):
            self.puntos = "Advantage"

    def ganarset(self, score1, score2):
        if (score1.puntos == 40) and (score2.puntos <= 30):
            self.puntos = "Set ganado por el jugador 1"
        elif (score2.puntos == 40) and (score1.puntos <= 30):
            self.puntos = "Set ganado por el jugador 2"

    def deuce(self, score1, score2):
        if (score1.puntos == 40) and (score2.puntos == 40):
            score1.puntos = "Deuce"
            score2.puntos = "Deuce"

    def ganarsetadvantage(self, score1, score2):
        if (score1.puntos == "Advantage") and (score2.puntos == 40):
            self.puntos = "Set ganado por el jugador 1"
