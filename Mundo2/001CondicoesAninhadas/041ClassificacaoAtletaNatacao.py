# Exercício Python 041: A Confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
import datetime

anoAtual = datetime.date.today().year
anoNascimento = int(input('Informe o ano de nascimento: '))

idade = anoAtual - anoNascimento

if idade <= 9:
    print('MIRIN')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')