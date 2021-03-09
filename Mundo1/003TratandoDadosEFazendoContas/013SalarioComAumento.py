salarioAtual = float(input('Informe o salário atual: '))
percentualAumento = float(input('Informe o parcentual de aumento: '))
valorDoAumento = salarioAtual * (percentualAumento / 100)
novoSalario = salarioAtual + valorDoAumento
print('O valor do aumento é de {:.2f}'.format(valorDoAumento))
print('O novo salário é de {:.2f}'.format(novoSalario))