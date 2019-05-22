from unittest import TestCase
from fruta import fruta

class TestFruta(TestCase):
    def test_pelar(self):
        dado = fruta('banano', 10)
        espero = True
        real = dado.pelar()

        self.assertEqual(real, espero)

        self.assertRaises(ValueError, dado.pelar)

    def test_cortar(self):
        dado = fruta('papaya', 1000)
        espero = 130
        real = dado.cortar(130)

        self.assertEqual(real, espero)

    def test_licuar(self):
        dado = fruta('manzana', 12)
        espero = 6
        real = dado.licuar(6)

        self.assertEqual(real, espero)
