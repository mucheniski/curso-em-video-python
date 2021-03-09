nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informa a nota 2: '))
media = (nota1 + nota2) / 2
print('Sua nota foi {:.1f} '.format(media))
if media >= 6.0:
    print('Sua nota foi boa!')
else:
    print('Estuda mais!')