from municipio import Municipio


class Distrito(Municipio):

    def __init__(self, enderecoPrefeitura, nome, populacao, area):
        Municipio.__init__(self, nome, populacao, area)
        self.enderecoPrefeitura = enderecoPrefeitura


@property
def enderecoPrefeitura(self):
    return self.enderecoPrefeitura


@enderecoPrefeitura.setter
def enderecoPrefeitura(self, enderecoPrefeitura):
    self.enderecoPrefeitura = enderecoPrefeitura
