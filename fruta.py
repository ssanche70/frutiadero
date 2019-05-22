class fruta:

    sabor = ''
    pelada = False
    cantidad = 0
    __TIPOS__ = {'banano': [5, 100], 'manzana': [6, 50], 'pera': [5, 70], 'piña': [60, 1500], 'papaya': [130, 2200]}

    def __init__(self, sabor, cantidad):

        self.sabor = sabor if sabor in self.__TIPOS__ else 'banano'
        self.cantidad = cantidad

    def pelar(self):

        if not self.pelada:
            self.pelada = True
            return self.pelada
        raise ValueError('La fruta ya esta pelada')

    def cortar(self, cantidad_usar):

        self.cantidad_usar = cantidad_usar

        if not self.pelada and cantidad_usar > 0:
            return cantidad_usar

        elif cantidad_usar <= 0:
            return 'No hay frutas'

        elif self.pelada:
            return 'La fruta se debe pelar'

    def licuar(self, cantidad_usar):

        self.cantidad_usar = cantidad_usar

        if not self.pelada and cantidad_usar > 0:
            return cantidad_usar

        elif self.pelada and cantidad_usar <= 0:
            return 'Así no se puede hacer jugo'
