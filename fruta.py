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

        if not self.pelada and cantidad_usar > 0 and self.sabor == 'papaya':
            return cantidad_usar * 130

        elif not self.pelada and cantidad_usar > 0 and self.sabor == 'banano':
            return cantidad_usar * 10

        elif cantidad_usar <= 0 or self.pelada:
            raise ValueError('No hay manera de proceder')

    def licuar(self, cantidad_usar):

        self.cantidad_usar = cantidad_usar

        if not self.pelada and cantidad_usar > 0:
            return cantidad_usar * 6

        elif self.pelada or cantidad_usar <= 0:
            raise ValueError('Así no se puede hacer jugo')
