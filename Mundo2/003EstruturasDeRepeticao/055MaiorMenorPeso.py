# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maiorPeso = 0
menorPeso = 0
for i in range(1,6):
    peso = float(input('Informe o {}º peso: '.format(i)))

    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso < menorPeso:
            menorPeso = peso
        if peso > maiorPeso:
            maiorPeso = peso
print('O maior peso foi {} e o menor foi {}'.format(maiorPeso, menorPeso))