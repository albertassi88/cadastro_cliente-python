def erro():
    try:
        numero = int(input('Digite uma opção:'))
    except ValueError:
        letra = input('Opção Inválida! Digite uma opção novamente.')
        while not letra.isdigit():
            letra = input('Opção Inválida! Digite uma opção novamente.')
        numero = int(letra)
    return numero


def telefone_erro():
    try:
        numero = int(input('Telefone: '))
    except ValueError:
        letra = input('Erro! Digite só números.')
        while not letra.isdigit():
            letra = input('Erro! Digite só numeros..')
        numero = int(letra)
    return numero

