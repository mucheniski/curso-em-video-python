# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = 0
quantidadeNumeros = 0
soma = 0
while numero != 999:
    numero = int(input('Informe um número (999 para sair): '))
    if numero != 999:
        quantidadeNumeros += 1
        soma += numero

print('Fim da programação!')
print('Foram digitados {} números, a soma deles é {}'.format(quantidadeNumeros, soma))