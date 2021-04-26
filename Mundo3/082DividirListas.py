# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
listaCompleta = list()
listaPares = list()
listaImpares = list()

while True:
    numero = int(input('Informe um número: '))
    listaCompleta.append(numero)

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break

for numero in listaCompleta:
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

print(f'Lista completa {listaCompleta}')
print(f'Lista pares {listaPares}')
print(f'Lista impares {listaImpares}')
print('Fim do programa')