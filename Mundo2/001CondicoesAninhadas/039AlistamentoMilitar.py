# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

anoAtual = datetime.date.today().year
anoNascimentoGafanhoto = int(input('Informe seu ano de nascimento pequeno gafanhoto: '))
sexo = str(input('Informe o sexo M ou F ')).upper()
idadeAlistamento = 18
idadeGafanhoto = anoAtual - anoNascimentoGafanhoto
prazoParaAlistar = 0

print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimentoGafanhoto, idadeGafanhoto, anoAtual))

if sexo == 'M':
    if idadeGafanhoto < idadeAlistamento:
        anosFaltantes = idadeAlistamento - idadeGafanhoto
        print('Ainda vai se alistar, faltam {} anos'.format(anosFaltantes))
        print('Você vai se alister em {}'.format(anoAtual + anosFaltantes))
    elif idadeGafanhoto > idadeAlistamento:
        anosAtrasados = idadeGafanhoto - idadeAlistamento
        print('Já passou do prazo para se alistar em {} anos'.format(anosAtrasados))
        print('Deveria ter se alistado em {}'.format(anoAtual - anosAtrasados))
    else:
        print('Corra para se alistar, seu país precisa de você!')
elif sexo == 'F':
    print('Você não precisa se alistar, é somente para homens!')
else:
    print('Esse sexo não existe pequeno gafanhoto!')
