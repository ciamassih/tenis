import unittest

from partido_tenis import Score

class PartidoTenis(unittest.TestCase):

    def test_inicio_partido(self):
        score = Score(0)
        self.assertEqual(score.player1, 0)
