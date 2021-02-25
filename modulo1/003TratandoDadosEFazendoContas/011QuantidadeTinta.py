base = float(input('Informe a medida da base da parede: '))
altura = float(input('Informe a medida da altura da parede: '))
area = base * altura
capacidadeLitroTinta = 2.0
quantidadeTintaNecessaria = area / capacidadeLitroTinta
print('A area é {:.2f} metros quadrados e a quantidade de tinta necessária é {:.2f} litros'.format(area, quantidadeTintaNecessaria))