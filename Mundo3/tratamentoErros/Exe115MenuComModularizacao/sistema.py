from lib.interface import *
from lib.arquivo import *
from time import sleep

nomeArquivo = 'pessoas.txt'

if not arquivoExiste(nomeArquivo):
    criarArquivo(nomeArquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if resposta == 1:
        lerArquivo(nomeArquivo)

    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo')
        break
    else:
        print('Digite uma opção válida')
    sleep(2)


