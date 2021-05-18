# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# O asterisco * significa que vai receber vários valores
from time import  sleep

def maior(* listaNumeros):

    maiorNumero = 0
    print('\nANALISANDO NUMEROS')
    for numero in listaNumeros:
        print(numero, end=' ', flush=True) # O flush True serve para as versões mais recentes, para que o sleep funcione
        sleep(0.3)

        if numero > maiorNumero:
            maiorNumero = numero

    print(f'\nO maior número é {maiorNumero}')


maior(10, 40, 2, 6, 8)