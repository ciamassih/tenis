import unittest

from partido_tenis import Tenis

class PartidoTenis(unittest.TestCase):

    def test_inicio_partido(self):
        tenis = Tenis()
        self.assertEqual("inicio de partido", tenis.score())
