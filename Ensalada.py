class Ensalada:

    nombre = ''
    tamano = ''
    ingredientes = ''
    crema = ''

    def __init__(self, nombre, tamano, ingredientes, crema):
        self.nombre = nombre
        self.tamano = tamano
        self.ingredientes = ingredientes
        self.crema = crema

    def alistar(self, nombre, tamano, ingredientes, crema):
        return f'Usted pidio un {nombre} de {tamano} Oz, con {ingredientes} y {crema} crema'