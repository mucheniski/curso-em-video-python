# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listaNumeros = list()

while True:
    numero = int(input('Informe um número: '))

    if numero not in listaNumeros:
        listaNumeros.append(numero)

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break
print(f'Os valores únicos digitados foram {listaNumeros}')
print('Fim do programa')