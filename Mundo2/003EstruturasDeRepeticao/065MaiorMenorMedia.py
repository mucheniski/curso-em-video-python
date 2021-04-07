# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = 'S'
numero = maior = menor = soma = contador = media = 0
while resposta == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    if contador == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    contador += 1
    resposta = str(input('Deseja continuar? S/N: ')).strip().upper()

media = soma / contador

print('Fim da programação')
print('Foram digitados {} números, o soma é {} e a média é {}'.format(contador, soma, media))
print('O número maior é {} e o menor é {}'.format(maior, menor))
