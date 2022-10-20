# Crie um while que digite e some todos so valores para sair usar o 999 sem o 999 somar.


cont = 0
n1 = 0
total = 0
while n1 != 999:
    n1 = int(input('digite um valor para somar --> '))
    if n1 == 999:
        break
    cont = cont + 1
    total = total + n1
print(f'você digitou {cont}x o total da soma foi {total}')
