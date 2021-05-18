# Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime

def validaSituacao(idade):
    situacao = 'OBRIGATÓRIO'
    if idade <= 16:
        situacao = 'NEGADO'
    if idade > 65:
        situacao = 'OPCIONAL'
    return situacao


anoAtual = datetime.date.today().year
anoNascimento = int(input('Informe o ano de nascimento: '))
idade = anoAtual - anoNascimento

status = validaSituacao(idade)
print(status)
