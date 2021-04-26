# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')) )

print('-'*100)
print('A) Quantas vezes apareceu o valor 9.')
print(numeros.count(9))
print('-'*100)
print('B) Em que posição foi digitado o primeiro valor 3.')
print(numeros.index(3))
print('-'*100)
print('C) Quais foram os números pares.')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
print('-'*100)