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
        dado = fruta('manzana', 4)
        espero = True
        real = dado.cortar()

        self.assertEqual(real, espero)

    def test_licuar(self):
        self.fail()
