class fruta:

    sabor = ''
    pelada = False
    cantidad = 2

    def __init__(self, sabor, pelada, cantidad):

        self.sabor = sabor
        self.cantidad = cantidad

    def pelar(self, pelada):

        if self.pelada:
            self.pelada = True
        else:
            self.pelada = False
        return self.pelada

    def cortar(self, cantidad):

        if self.pelada and cantidad > 0:
            cantidad -= 1
            return 4.0
        elif cantidad <= 0:
            return 'No hay frutas'
        elif not self.pelada:
            'La fruta se debe pelar'

    def licuar(self, cantidad):
        if self.pelada and cantidad > 0
