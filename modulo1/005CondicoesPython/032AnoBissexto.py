import datetime

#  todos os anos múltiplos de 4 que também não são múltiplos de 100,
#  com exceção dos múltiplos de 400, deverão ser anos bissextos.

anoAtual = datetime.date.today().year

ano = int(input('Informe o ano que quer analisar. Para ano atual coloque 0: '))

if ano == 0:
    ano = anoAtual

print('Verificando o ano {}'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

