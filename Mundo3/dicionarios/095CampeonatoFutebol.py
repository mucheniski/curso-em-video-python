# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
campeonato = list()
dadosJogador = dict()
saldoDeGols = 0

while True:

    dadosJogador['nomeJogador'] = str(input('Informe o nome do jogador: '))
    dadosJogador['quantidadePartidas'] = int(input('Informe a quantidade de partidas: '))

    if dadosJogador['quantidadePartidas'] > 0:
        for partida in range(1, dadosJogador['quantidadePartidas'] + 1):
            quantidadeGols = int(input(f'Quantos gols foram feitos na partida {partida}? '))
            saldoDeGols += quantidadeGols

    dadosJogador['saldoGols'] = saldoDeGols
    saldoDeGols = 0

    campeonato.append(dadosJogador.copy())

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break

print('Fim do programa')
print(campeonato)