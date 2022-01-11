import unittest

from partido_tenis import Score

class PartidoTenis(unittest.TestCase):

    def test_puntaje_en_0(self):
        score1 = Score(0)
        self.assertEqual(score1.puntos, 0)

    def test_puntaje_en_15(self):
        score1 = Score(15)
        self.assertEqual(score1.puntos, 15)

    def test_puntaje_en_0_con_los_2_jugadores(self):
        score1 = Score(0)
        score2 = Score(0)
        self.assertEqual(score1.puntos, 0)
        self.assertEqual(score2.puntos, 0)

    def test_puntaje_en_15_a_30(self):
        score1 = Score(15)
        score1.anotacion(15)
        self.assertEqual(score1.puntos, 30)

    def test_puntaje_en_30_a_40(self):
        score1 = Score(30)
        score1.anotacion(10)
        self.assertEqual(score1.puntos, 40)

    def test_punto_ganador(self):
        score1 = Score(40)
        score1.ganarset()
        self.assertEqual(score1.puntos, "Set ganado")