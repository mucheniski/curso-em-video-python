# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = int(input('Informe o tamanho da primeira reta: '))
reta2 = int(input('Informe o tamanho da segunda reta: '))
reta3 = int(input('Informe o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta1 < reta1 + reta2:
    print('Os valores podem formar um triângulo!')
else:
    print('Os valores não podem formar um triângulo!')