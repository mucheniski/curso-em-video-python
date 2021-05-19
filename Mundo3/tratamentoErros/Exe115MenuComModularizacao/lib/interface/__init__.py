def linha(tamanho = 42):
    print('-'*tamanho)


def cabecalho(texto):
    linha()
    print(texto.center(42))
    linha()


def leiaInt(mensgem):
    while True:
        try:
            numero = int(input(mensgem))
        except ValueError as erro:
            print(f'Deu ruim {erro.__class__}')
            continue
        else:
            return numero


def menu(lista):
    cabecalho('SISTEMA ARQUIVO V.1.0')
    opcao = 1
    for item in lista:
        print(f'{opcao} - {item}')
        opcao += 1
    linha()
    opcao = leiaInt('Sua opçao: ')
    return opcao