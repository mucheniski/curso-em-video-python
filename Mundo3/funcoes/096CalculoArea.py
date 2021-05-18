# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(base, altura):
    area = base * altura
    print(f'base {base} * {altura} area total = {area}')


base = int(input('Informe a base: '))
altura = int(input('Informe a altura: '))
area(base, altura)
