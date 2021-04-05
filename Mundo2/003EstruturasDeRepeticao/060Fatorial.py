# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
numero = int(input('Informe um número para saber seu fatorial: '))
fatorial = factorial(numero)
print('O fatorial do numero {} é {}'.format(numero, fatorial))

print('Vamos conferir!')
contador = numero

# Multiplicação nunca pode começar com zero
total = 1
while contador > 0:
    total *= contador
    # Não pular linha
    print('{}'.format(contador), end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    contador -= 1
print(total)
