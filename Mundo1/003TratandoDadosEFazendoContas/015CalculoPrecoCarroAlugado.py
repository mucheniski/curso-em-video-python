kmPercorridos = float(input('Qual a quantidade de KM percorrida? '))
diasAlugados = int(input('Qual a quantidade de dias alugados? '))
custoPorDia = 60.0
custoPorKM = 0.15
valorAPagar = (diasAlugados * custoPorDia) + (kmPercorridos * custoPorKM)
print('O valor a pagar é de R${:.2f}'.format(valorAPagar))