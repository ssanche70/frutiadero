class Jugo:

    nombre = ''
    tamano = ''
    ingredientes = ''
    azucar = 0
    porcentajeagua = 0

    def __init__(self, nombre, tamano, ingredientes, azucar, pocentajeagua):
        self.nombre = nombre
        self.tamano = tamano
        self.ingredientes = ingredientes
        self.azucar = azucar
        self.porcentajeagua = pocentajeagua

    def preparar(self, nombre, tamano, ingredientes, azucar, porcentajeagua):
        return f'Ested eligió {nombre} de {tamano} Oz con {ingredientes}, {azucar} azucar y {porcentajeagua} % de agua'