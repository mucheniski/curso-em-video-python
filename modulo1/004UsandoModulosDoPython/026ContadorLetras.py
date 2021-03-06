# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra “A”, em que posição ela aparece a primeira
# vez e em que posição ela aparece a última vez.
frase = str(input('Informe a frase: ')).strip().upper()
print('A letra A aparece {} vezes!'.format(frase.count('A')))
print('A primeira vez aparece em {} '.format(frase.find('A')))
print('A última vez aparece em {} '.format(frase.rfind('A')))