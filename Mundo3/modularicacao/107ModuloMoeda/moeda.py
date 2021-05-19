# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(valor, formatar=False):
    retorno = valor + 1
    if formatar:
        return formataMoeda(retorno)
    else:
        return retorno


def diminuir(valor, formatar=False):
    retorno = valor - 1
    if formatar:
        return formataMoeda(retorno)
    else:
        return retorno


def dobro(valor, formatar=False):
    retorno = valor * 2
    if formatar:
        return formataMoeda(retorno)
    else:
        return retorno


def metade(valor, formatar=False):
    retorno = valor / 2
    if formatar:
        return formataMoeda(retorno)
    else:
        return retorno


def formataMoeda(valor, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.', ',')
