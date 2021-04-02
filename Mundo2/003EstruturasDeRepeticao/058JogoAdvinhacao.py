# Exercício Python 58: Melhore o jogo do DESAFIO 28
# onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random

numeroSorteado = random.randint(0, 10)
qtdPalpites = 0

print('Número sorteado {}'.format(numeroSorteado))

print('Tente acertar o número')
numeroEscolhido = int(input('Escolha um número: '))
while numeroEscolhido != numeroSorteado:
    numeroEscolhido = int(input('Eroooooou! Escolha outro número: '))
    qtdPalpites += 1
print('Acertou com {} palpites'.format(qtdPalpites))