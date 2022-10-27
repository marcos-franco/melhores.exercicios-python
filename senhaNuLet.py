# esse programa só deixa a senha roda se tiver letra e numeros.


numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

senhaValida = 0

while senhaValida == 0:
    senha = input("Digite uma senha valida")
    temLetra = False
    temNumero = False

    for letra in senha:


        if letra in (numeros):
            temNumero = True

        if letra.isalpha():
            temLetra = True

        if (temLetra == 1) and (temNumero == 1):
            senhaValida = 1
            print("Logado com sucesso !")
            break
