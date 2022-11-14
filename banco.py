class Conta:
    
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo


    def extrato(self):
        print(f'Saldo : R$ {self.saldo}')
        
    def deposito(self, valor):
        self.saldo += valor
        print(f'{self.titular} deposito realizado')
    
    def sacar(self, valor):
        self.saldo -= valor
        print(f'{self.titular} saque realizado')
        