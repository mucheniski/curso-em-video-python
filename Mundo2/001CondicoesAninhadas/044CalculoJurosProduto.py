# Exercício Python 44: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Informe o valor do produto: '))
tipoPagamento = int(input('Informe o tipo de pagamento (1-À vista | 2-Parcelado): '))
valorDoDesconto = 0
valorFinal = 0

if tipoPagamento == 1:
    print('Selecionado Pagamento À vista!')
    formaPagamento = int(input('Informe a forma de pagamento (1-Dinheiro | 2-Cartão): '))

    if formaPagamento == 1:
        print('Forma de pagamento Dinheiro')
        valorDoDesconto = valorProduto * 0.1
        valorFinal = valorProduto - valorDoDesconto
        print('Valor do produto R${:.2f} menos desconto de R${:.2f} = R${:.2f}'.format(valorProduto, valorDoDesconto, valorFinal))
    elif formaPagamento == 2:
        print('Forma de pagamento Cartão')
        valorDoDesconto = valorProduto * 0.05
        valorFinal = valorProduto - valorDoDesconto
        print('Valor do produto R${:.2f} menos desconto de R${:.2f} = R${:.2f}'.format(valorProduto, valorDoDesconto, valorFinal))
    else:
        print('Forma de pagamento selecionada não existe')

elif tipoPagamento == 2:
    print('Selecionado Pagamento Parcelado')
    qtdeParcelas = int(input('Informe a quantidade de parcelas: '))
    valorParcelas = 0

    if qtdeParcelas >= 1 and qtdeParcelas <= 2:
        valorParcelas = valorProduto / qtdeParcelas
        print('O valor do produto R${:.2f} dividido em {} parcelas fica R${:.2f} a parcela'.format(valorProduto, qtdeParcelas, valorParcelas))
    elif qtdeParcelas >= 3:
        valorComJuros = valorProduto * 1.2
        valorParcelas = valorComJuros / qtdeParcelas
        print('O valor do produto R${:.2f} dividido em {} parcelas com juros de 20% fica R${:.2f} a parcela'.format(valorProduto, qtdeParcelas, valorParcelas))
    else:
        print('A quantidade de parcelas precisa ser um valor positivo maior que Zero')

else:
    print('Tipo de pagamento não existe')
