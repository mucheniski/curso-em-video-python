# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe o sexo M ou F ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Valor inválido, informe o sexo M ou F: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))