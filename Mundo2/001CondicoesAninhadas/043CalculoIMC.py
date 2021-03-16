# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura
# de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# O IMC é a relação entre peso e altura e o cálculo é feito de acordo com a fórmula:
# IMC = peso/ (altura x altura), devendo o peso estar em kg e a altura em metro,
# e o resultado é dado em kg/m2
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
IMC = peso / (altura ** 2)

print('O IMC é de {:.2f}'.format(IMC))

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC <= 25:
    print('Peso ideal')
elif IMC <= 30:
    print('Sobrepeso')
elif IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')