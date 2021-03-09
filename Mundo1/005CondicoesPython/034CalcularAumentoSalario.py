# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Infore o salário: '))
valorAumento = 0
novoSalario = 0
percentualAumento = 0.0
if salario > 1250.0:
    percentualAumento = 0.1
else:
    percentualAumento = 0.15

valorAumento = salario * percentualAumento
novoSalario = salario + valorAumento

print('-'*50)
print('O salario foi de {:.2f}'.format(salario))
print('O percentual de aumento foi de {}%'.format(percentualAumento * 100))
print('O valor do aumento foi {:.2f}'.format(valorAumento))
print('O novo salário é {:.2f}'.format(novoSalario))
print('-'*50)