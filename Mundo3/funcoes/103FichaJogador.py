# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='Desconhecido', totalGols=0):

    print(f'O jogador {nome} fez {totalGols} gols')


nome = str(input('Informe o nome do jogador: '))
gols = str(input('Informe a quantidade de gols: '))

if nome.strip() == '':
    nome = 'Desconhecido'

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)