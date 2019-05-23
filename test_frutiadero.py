from unittest import TestCase
from Ensalada import Ensalada
from Jugo import  Jugo


class TestFrutiadero(TestCase):
    def test_preparar(self):
        dado = Ensalada('Elixir', 9, 'Mango Piña Maracuya', 'con')
        espero = 'Usted pidio un Elixir de 9 Oz, con Mango Piña Maracuya y con crema'
        real = dado.alistar('Elixir', 9, 'Mango Piña Maracuya', 'con')

        self.assertEqual(real, espero)

        dado = Jugo('Bosque Negro', 7, 'Arándanos Mora Agraz', 'con', 30)
        espero = 'Ested eligió Bosque Negro de 7 Oz con Arándanos Mora Agraz, con azucar y 30 % de agua'
        real = dado.preparar('Bosque Negro', 7, 'Arándanos Mora Agraz', 'con', 30)

        self.assertEqual(real, espero)