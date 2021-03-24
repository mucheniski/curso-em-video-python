# Exercício Python 52: Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.
contador = 0
numero = int(input('Informe o número: '))
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        contador += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero, contador))
if contador == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')