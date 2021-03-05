# Exercício Python 24: Crie um programa que leia o nome de
# uma cidade diga se ela começa ou não com o nome “SANTO”.
nomeCidade = str(input('Informe o nome da cidade: ')).strip()
print(nomeCidade[:5].upper() == 'SANTO')
