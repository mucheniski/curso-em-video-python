def mostraLinha():
    print('-'*50)


def divideTela():
    print()
    print('='*100)
    print()


def mensagem(texto):
    print('-' * 50)
    print(texto)
    print('-' * 50)


# Entre as funções e o programa principal o pycharm pede 2 linhas vazias
mostraLinha()
print('Teste linha')
mostraLinha()

divideTela()

mensagem('SISTEMA DE ALUNOS')
