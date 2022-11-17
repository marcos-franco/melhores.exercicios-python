class Municipio:

    def __init__(self, nome, populacao, area):
        self.__nome = nome
        self.__populacao = populacao
        self.__area = area

    @property  # propriedades / posso ver o nome
    def nome(self):
        return self.__nome

    @nome.setter  # --> agora posso trocar o nome
    def nome(self, nome):
        self.__nome = nome

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area
