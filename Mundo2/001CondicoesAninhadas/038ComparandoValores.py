# Exercício Python 038: Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

print('Os valores escolhidos foram {} e {}'.format(numero1, numero2))
if numero1 > numero2:
    print('O primeiro valor é maior')
elif numero2 > numero1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
