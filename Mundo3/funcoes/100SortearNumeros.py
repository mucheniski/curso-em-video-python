# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista):
    for i in range(1, 6):
        lista.append(randint(1, 100))
    print(f'Numeros sorteados {lista}')


def somaPares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f'O valor da soma dos pares é {soma}')


listaNumeros = list()
sorteia(listaNumeros)
somaPares(listaNumeros)


