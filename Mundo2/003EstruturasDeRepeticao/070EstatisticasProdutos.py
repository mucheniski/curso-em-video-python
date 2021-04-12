# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
nomeProduto = nomeProdutoMaisBarato = ''
precoProduto = precoProdutoMaisBarato = totalCompra = 0.0
contadorMaisDe1000 = 0
while True:
    nomeProduto = str(input('Informe o nome do produto: ')).strip()
    precoProduto = float(input('Informe o preço do produto: '))

    if totalCompra == 0:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto

    if precoProduto > 1000:
        contadorMaisDe1000 += 1

    if precoProduto < precoProdutoMaisBarato:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto

    totalCompra += precoProduto

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break

print('Fim do programa')
print(f'A) qual é o total gasto na compra. {totalCompra}')
print(f'B) quantos produtos custam mais de R$1000. {contadorMaisDe1000}')
print(f'C) qual é o nome do produto mais barato. {nomeProdutoMaisBarato}')