# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

campeonato = dict()
saldoDeGols = 0

campeonato['nomeJogador'] = str(input('Informe o nome do jogador: '))
campeonato['quantidadePartidas'] = int(input('Informe a quantidade de partidas: '))

if campeonato['quantidadePartidas'] > 0:
    for partida in range(1,campeonato['quantidadePartidas']+1):
        quantidadeGols = int(input(f'Quantos gols foram feitos na partida {partida}? '))
        saldoDeGols += quantidadeGols

campeonato['saldoDeGols'] = saldoDeGols

print(campeonato)
