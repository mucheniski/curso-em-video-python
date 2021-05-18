# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(inicio, fim, passo):

    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(i, end=' ')
    if fim < inicio:
        for i in range(inicio, fim, -passo): # passo negativo decrementa o valor
            print(i, end=' ')


def pulaLinha():
    print()
    print('='*50)
    print()


contador(1, 10, 1)
pulaLinha()

contador(10, 1, 2)
pulaLinha()
