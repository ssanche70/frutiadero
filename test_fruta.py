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
        real = dado.cortar(1)

        self.assertEqual(real, espero)

        dado = fruta('banano', 1000)
        espero = 10
        real = dado.cortar(1)

        self.assertEqual(real, espero)

        dado = fruta('pera', 0)

        with self.assertRaises(ValueError):
            dado.cortar(0)

        # dado = fruta('pera', 4)
        #
        # with self.assertRaises(ValueError):
        #     dado.pelar()

    def test_licuar(self):
        dado = fruta('manzana', 12)
        espero = 6
        real = dado.licuar(1)

        self.assertEqual(real, espero)

        dado = fruta('piña', 30)
        espero = 12
        real = dado.licuar(2)

        self.assertEqual(real, espero)

        # self.assertRaises(ValueError, dado.pelar)

        dado = fruta('manzana', 12)

        with self.assertRaises(ValueError):
            dado.licuar(0)

