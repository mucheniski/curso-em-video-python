from Mundo3.tratamentoErros.Exe115MenuComModularizacao.lib.interface import *


def arquivoExiste(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'rt') # Abrir para leitura Read Text rt
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'wt+') # Excreve o arquivo Write wt e se não existir cria +
        arquivo.close()
    except Exception as erro:
        print(f'Deu ruim pra criar o arquivo {erro.__class__}')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso')


def lerArquivo(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'rt')
    except Exception as erro:
        print(f'Deu ruim pra ler o arquivo {erro.__class__}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(arquivo.read())