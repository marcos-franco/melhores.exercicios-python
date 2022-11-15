class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = lado * lado

    def retorna_area(self):
        print(self.area)


quadrado = Quadrado(2)
quadrado.retorna_area()


class Idade:
    def __init__(self, nascimento, ano):
        self.nascimento = nascimento
        self.ano = ano

    def SuaIdade(self):
        print(self.ano - self.nascimento)


idade = Idade(1987, 2022)
idade.SuaIdade()
