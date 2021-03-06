# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Informe a velocidade: '))
limiteDeVelocidade = 80.0
if velocidade > limiteDeVelocidade:
    valorMulta = (velocidade - limiteDeVelocidade) * 7.00
    print('Você foi multado mothafucker, vai pagar R$ {:.2f}'.format(valorMulta))
else:
    print('Tenha uma boa viagem!')