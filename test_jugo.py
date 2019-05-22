from unittest import TestCase
from Jugo import Jugo

class TestJugo(TestCase):
    def test_preparar(self):
        dado = Jugo('Bosque Negro', 7, 'Arándanos Mora Agraz', 'con', 30)
        espero = 'Ested eligió Bosque Negro de 7 Oz con Arándanos Mora Agraz, con azucar y 30 % de agua'
        real = dado.preparar('Bosque Negro', 7, 'Arándanos Mora Agraz', 'con', 30)

        self.assertEqual(real, espero)

        dado = Jugo('Bosque Blanco', 11, 'Corozo Araza Lulo', 'con', 50)

        with self.assertRaises(ValueError):
            dado.preparar('Bosque Blanco', 12, 'Corozo Araza Lulo', 'con', 5)
