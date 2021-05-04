# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint

print('================MEGA SENA================')
qtdJogos = int(input('Quantos jogos você vai querer fazer? '))
for numeroJogo in range(0, qtdJogos):
    print('=' * 50)
    print(f'Jogo número {numeroJogo+1}')

    for i in range(0, 6):
        jogada = randint(1, 60)
        print(jogada, end=' ')
    print()

print('Fim da mega sena!')
