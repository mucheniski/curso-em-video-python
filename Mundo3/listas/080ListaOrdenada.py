# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = list()

for i in range(0,5):
    numero = int(input('Informe um número: '))

    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posicao {posicao}')
                break
            posicao += 1
print(f'Os números digitados foram {lista}')

