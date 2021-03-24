# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

anoAtual = datetime.date.today().year

qtdeMaiores = 0
qtdeMenores = 0
for i in range(1,8):
    anoNascimento = int(input('Informe o {}º ano de nascimento: '.format(i)))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        qtdeMaiores += 1
    else:
        qtdeMenores += 1

print('O total de menores é {} e o total de maiores é {}'.format(qtdeMenores, qtdeMaiores))
