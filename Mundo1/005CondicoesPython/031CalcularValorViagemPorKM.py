# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distanciaKM = float(input('Informe a distancia em KM: '))
valorViagem = 0.0

if distanciaKM <= 200.0:
    valorViagem = distanciaKM * 0.5
else:
    valorViagem = distanciaKM * 0.45

print('O Valor da viagem é de R$ {:.2f}'.format(valorViagem))
