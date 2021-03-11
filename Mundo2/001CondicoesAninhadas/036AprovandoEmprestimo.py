# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.
valorCasa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos vai pagar? '))
prestacaoMensal = valorCasa / anos
if prestacaoMensal > (salario * 0.3):
    print('Empréstimo \033[32m APROVADO \033[m')
else:
    print('Emprestimo \033[31m NEGADO \033[m')