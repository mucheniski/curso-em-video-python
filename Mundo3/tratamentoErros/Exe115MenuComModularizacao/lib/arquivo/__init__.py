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
        for linha in arquivo:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '') # Para tirar a quebra de linha da idade
            print(f'{dados[0]:<30} {dados[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrarPessoa(nomeArquivo, nomePessoa='Nem nome tem', idade=0):
    try:
        arquivo = open(nomeArquivo, 'at') # append text at, adicionar
    except Exception as erro:
        print(f'Deu ruim pra adicionar {erro.__class__}')
    else:
        try:
            arquivo.write(f'{nomePessoa};{idade}\n')
        except Exception as erro:
            print(f'Deu ruim pra escrever os dados')
        else:
            print(f'Novo registros de {nomePessoa} cadastrado com sucesso')
            arquivo.close()

