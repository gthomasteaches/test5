from modelo.canasta import Canasta


class Naranja:
    def __init__(self):
        # self.__privado = 0  # atributo privado
        self.peso = 0
        self.granja = None
        self.fecha_cosecha = None
        self.canasta = None

    def recoger(self, canasta: Canasta):
        self.canasta = canasta
        canasta.naranjas.append(self)
        print("Naranja agregada")

    def exprimir(self):
        return self.peso * 0.9
