# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for i in range(1, 7):
    numero = int(input('Informe o número: '))
    if numero % 2 == 0:
        contador += 1
        soma += numero
print('Foram digitados {} números pares, a soma é {}'.format(contador, soma))
