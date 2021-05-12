# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print('Valores sorteados:')
for jogador, jogada in jogadas.items():
    print(f'O Jogador {jogador} tirou {jogada}')
    sleep(1)
# Ordenar em ordem crescente o dicionário
# o 0 é chave o 1 é valor para o itemgetter
ranking = dict()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('='*50)
for nome, pontos in ranking:
    print(f'Posicao {nome} com {pontos} pontos')