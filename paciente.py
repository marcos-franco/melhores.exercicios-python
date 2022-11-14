

class Paciente:
    def __init__(self, nome, idade, cpf, email):
        print('Acessei o construtor')
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email


from paciente import Paciente


paciente = Paciente('paulo', 33, '001.002.003.45', 'paulo.roberto@gmail')
print(paciente.nome)
print(paciente.idade)
