valorProduto = float(input('Informe o valor do produto: '))
percentualDesconto = 0.05
valorPercentual = valorProduto * percentualDesconto
valorComDesconto = valorProduto - valorPercentual

print('O valor do desconto é de {:.2f}'.format(valorPercentual))
print('O valor do produto com desconto é {:.2f}'.format(valorComDesconto))