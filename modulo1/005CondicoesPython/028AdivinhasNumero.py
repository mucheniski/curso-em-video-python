# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

numeros = [0, 1, 2, 3, 4, 5]
numeroSorteado = random.choice(numeros)
# print('Numero sorteado: {}'.format(numeroSorteado))
numeroEscolhido = int(input('Escolha um número: '))
if numeroEscolhido == numeroSorteado:
    print('Acerto miseravi!')
else:
    print('Eroooooouu!')