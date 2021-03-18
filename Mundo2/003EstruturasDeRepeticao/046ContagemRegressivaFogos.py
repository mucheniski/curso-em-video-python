# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro
# de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(0.5)
print('')
# Rojão 12 Tiros
print('POW....')
sleep(1)
for i in range(0,12):
    print('*TA*')
sleep(1)
print('BOOOOOM!!!*******')