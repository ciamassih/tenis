import unittest

from partido_tenis import Score

class PartidoTenis(unittest.TestCase):

    def test_puntaje_en_0(self):
        score1 = Score(0)
        self.assertEqual(score1.puntos, 0)

    def test_puntaje_en_15(self):
        score1 = Score(15)
        self.assertEqual(score1.puntos, 15)

    def test_puntaje_en_15_a_30(self):
        score1 = Score(15)
        score1.anotacion(score1)
        self.assertEqual(score1.puntos, 30)

    def test_puntaje_en_30_a_40(self):
        score1 = Score(30)
        score1.anotacion(score1)
        self.assertEqual(score1.puntos, 40)

    def test_punto_ganador_por_jugador_1(self):
        score1 = Score(40)
        score2 = Score(15)
        score1.ganarset(score1, score2)
        self.assertEqual(score1.puntos, "Set ganado por el jugador 1")

    def test_punto_ganador_por_jugador_2(self):
        score1 = Score(30)
        score2 = Score(40)
        score2.ganarset(score1, score2)
        self.assertEqual(score2.puntos, "Set ganado por el jugador 2")

    def test_puntaje_en_0_primer_punto_jugador_2(self):
        score1 = Score(0)
        score2 = Score(0)
        score2.anotacion(score2)
        self.assertEqual(score1.puntos, 0)
        self.assertEqual(score2.puntos, 15)

    def test_puntaje_40_40(self):
        score1 = Score(40)
        score2 = Score(30)
        score2.anotacion(score2)
        score1.deuce(score1, score2)
        self.assertEqual(score1.puntos, "Deuce")
        self.assertEqual(score2.puntos, "Deuce")

    def test_puntaje_advantage_jugador_1(self):
        score1 = Score(40)
        score2 = Score(40)
        score1.anotacion(score1)
        self.assertEqual(score1.puntos, "Advantage")
        self.assertEqual(score2.puntos, 40)