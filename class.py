class Paciente:

    def __init__(self, nome, idade, cpf, email):
        print('Acessei o construtor')
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
