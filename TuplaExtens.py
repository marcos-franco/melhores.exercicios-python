# usando tupla digita um numero e o programa vai  printar ele por extenso.

Cont = ('zero', 'um', 'dois', 'treis', 'quantro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um numero entre 0 e 20 : '))
    if 0 <= num <= 20:
        break
print(f'o numero que vc digitou foi : {Cont[num]} ')
