# esse programa ler se e homem ou mulher e separa a media salarial deles.



totalM = 0
totalF = 0
i2 = 0
sexo = 0
masc = 0
fem = 0
i = 0
salarioM = 0
salarioF = 0
cont = 0
mediaM = 0
mediaF = 0

while i2 < 4:
    i2 = i2 + 1
    sexo = int(input('Digite [1] masculino / Digite [2] feminino --> '))
    if sexo == 1:
        masc = masc + sexo
        salarioM = int(input('1 Qual e o valor do salario --> '))
        totalM = totalM + salarioM
        i = i + 1
    else:
        fem = fem + sexo
        salarioF = int(input('2 Qual e o valor do salario --> '))
        totalF = totalF + salarioF
        cont = cont + 1
mediaM = totalM / i
mediaF = totalF / cont

print(
    f'A media entre os salarios maculino e de {mediaM} do feminino e de {mediaF}.')
