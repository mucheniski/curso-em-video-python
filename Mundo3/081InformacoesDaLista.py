# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break
print('Todos os números foram inseridos!')
print(f'A) Quantos números foram digitados {len(lista)}')
lista.sort(reverse=True)
print(f'B) A lista de valores, ordenada de forma decrescente. {lista}')

print('C) Se o valor 5 foi digitado e está ou não na lista.')
if 5 in lista:
    print('Sim tem 5 na lista!')
else:
    print('Não foi digitado 5 na lista!')
