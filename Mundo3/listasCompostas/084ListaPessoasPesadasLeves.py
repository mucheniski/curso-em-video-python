# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
listaPessoas = list()
dados = list()
contador = 0
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(float(input('Informe o peso: ')))

    if len(listaPessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    listaPessoas.append(dados[:])
    dados.clear()
    contador += 1

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break

print(f'Foram cadastradas {contador} pessoas')
print(f'O maior peso foi {maiorPeso}')
print(f'O menor peso foi {menorPeso}')
print('Fim do programa')
