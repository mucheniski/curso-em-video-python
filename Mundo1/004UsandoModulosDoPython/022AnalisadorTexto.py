# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras no total (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
# nome = input('Informe um nome: ')
nome = 'Diego Mucheniski'
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
nomeSemEspacos = nome.strip()
nomeSemEspacos = nomeSemEspacos.replace(" ", "")
nomeCompleto = nome.split()
primeiroNome = nomeCompleto[0]

print('O nome informado foi {} '.format(nome))
print('Nome com letras maiúsculas {} '.format(nomeMaiusculo))
print('Nome com letras minúsculas {} '.format(nomeMinusculo))
print('Nome sem espaços {} '.format(nomeSemEspacos))
print('O total de letras do nome é {} '.format(len(nomeSemEspacos)))
print('Nome completo divido {} '.format(nomeCompleto))
print('Primeiro nome {} '.format(primeiroNome))
print('Total de letras do primeiro nome {} '.format(len(primeiroNome)))

