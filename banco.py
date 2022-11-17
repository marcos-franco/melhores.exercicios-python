class Conta:

    taxa = 0.50

    @staticmethod
    def retornaCodigoBanco():
        return '345'

# Atributos de Istacias
    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero     # protegida (protected)
        self.titular = titular    # publica (public)
        self.__saldo = saldo      # privada (private)

    def extrato(self):
        print(f'Saldo : R$ {self.__saldo}')

    def deposito(self, valor):
        self.__saldo += valor
        print(f'{self.titular} deposito realizado')

    def sacar(self, valor):
        self.__saldo -= valor
        print(f'{self.titular} saque realizado')

    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.deposito(valor)


conta1 = Conta(123, 'Paulo Roberto', 3000)
conta2 = Conta(124, 'Pedro Souza', 3000)
print(conta1.__dict__)
print(conta2.__dict__)
conta1.transferir(300, conta1, conta2)
conta1.extrato()
conta2.extrato()
