# com esse programa o usuario pode escolher sua senha e seu usuaria para entra.


usuario = input('ESCOLHA UM NOME DE USUARIO --> ')
escolhasenha = input('ESCOLHA SENHA DE USUARIO --> ')

for i in range(0, 3):
    nome = input('DIGITE NOME DE USUARIO --> ')
    senha = input('DIGITE A SENHA DO USUARIO --> ')
    if usuario == nome and escolhasenha == senha:
        print('SENHA ESTAR CERTA !\n ')
        teste = input('O QUE BUSCA NO SITE --> ')

    else:
        print('SENHA OU USUARIO ERRADO  ')
        i = i + 1
        if i == 3:
            print(f'SEU USUARIO ESTAR BLOQUEADO ERRO {i}')
