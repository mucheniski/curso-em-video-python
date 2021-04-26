# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtosPrecos = ('Notebook', 4000.00, 'Monitor', 450.00, 'Mouse', 90.00, 'Fone', 200.00)
# Se estiver em uma posição par é o nome do produto.
for posicao in range(0, len(produtosPrecos)):
    if posicao % 2 == 0:
        print(f'{produtosPrecos[posicao]} ', end='')
    else:
        print(f'R$ {produtosPrecos[posicao]}')
