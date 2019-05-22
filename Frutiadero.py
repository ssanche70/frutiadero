class Frutiadero:

     nombre = ''
     inventario = {'banano': [5, 100], 'manzana': [6, 50], 'pera': [5, 70], 'piña': [60, 1500], 'papaya': [130, 2200]}

     def __init__(self, nombre):

         self.nombre = nombre

     def preparar(self, tipo, ingredientes):