# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numeroReal = float(input('Informe um número real: '))
porcaoInteira = math.trunc(numeroReal)
print('O valor digitado foi {} e a sua porção interia é {}'.format(numeroReal, porcaoInteira))

# ou pode ser só com a lib específica
from math import trunc

numeroReal = float(input('Informe um número real: '))
porcaoInteira = trunc(numeroReal)
print('O valor digitado foi {} e a sua porção interia é {}'.format(numeroReal, porcaoInteira))
