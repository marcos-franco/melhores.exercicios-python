# essa função fala se um numero e par ou impar e para sair dela só digitando.


def par_impar():
    n1 = 0
    while n1 != 99:
        n1 = int(input('Digita um Numero --> '))
        print('Para sair digit 99')
        if (n1 % 2) == 0:
            print(f'{n1} é par')
        else:
            print(f'impar {n1}')


par_impar()
