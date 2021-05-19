# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(valor):
    return valor + 1


def diminuir(valor):
    return valor - 1


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def formataMoeda(valor, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.', ',')
