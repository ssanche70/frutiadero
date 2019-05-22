from unittest import TestCase
from Ensalada import Ensalada

class TestEnsalada(TestCase):
    def test_alistar(self):
        dado = Ensalada('Elixir', 9, 'Mango Piña Marauya', 'con')
        espero = 'Usted pidio un Elixir de 9 Oz, con Mango Piña Maracuya y con crema'
        real = dado.alistar('Elixir', 9, 'Mango Piña Maracuya', 'con')

        self.assertEqual(espero, real)

        dado = Ensalada('Margarita', 14, 'Pera Banano Manzana', 'con')

        with self.assertRaises(ValueError):
            dado.alistar('Margarita', 14, 'Pera Banano Manzana', 'con')

