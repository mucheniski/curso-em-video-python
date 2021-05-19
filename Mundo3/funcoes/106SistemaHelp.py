# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.


def customHelp(functionName, cor):
    print(cor)
    print('='*100)
    print(f'AJUDA COM A FUNÇÃO {functionName.__name__}')
    print('=' * 100)
    print(cores['fecha'])
    help(functionName)


cores = {
    'vermelho': '\033[0;30;41m',
    'verde':    '\033[0;30;41m',
    'amarelo':  '\033[0;30;43m',
    'azul':     '\033[0;30;44m',
    'roxo':     '\033[0;30;45m',
    'branco':   '\033[0;30m',
    'fecha':    '\033[m'
}


while True:
    funcao = str(input('Informe a função: '))

    if funcao == 'FIM':
        break

    cor = str(input('Informe a cor'))
    customHelp(print, cores[cor])