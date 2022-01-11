import unittest

from partido_tenis import Score

class PartidoTenis(unittest.TestCase):

    def test_puntaje_en_0(self):
        score1 = Score(0)
        self.assertEqual(score1.puntos, 0)