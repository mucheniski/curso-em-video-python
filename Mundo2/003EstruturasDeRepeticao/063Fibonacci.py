# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

numero = int(input('Quantos termos você quer mostrar?: '))
termoAnterior = 0
termoAtual = 1
contador = 3
print('{} => {}'.format(termoAnterior, termoAtual), end='')
while contador <= numero:
    novoTermo = termoAnterior + termoAtual
    print(' => {}'.format(novoTermo), end='')
    termoAnterior = termoAtual
    termoAtual = novoTermo
    contador += 1
print(' => FIM')
