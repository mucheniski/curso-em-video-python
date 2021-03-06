# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# nomeCompleto = str(input('Informe o nome completo: ')).upper().strip()
nomeCompleto = 'Bruna Duarte Mucheniski'
nomes = nomeCompleto.split()
primeiroNome = nomes[0]
ultimoNome = nomes[len(nomes)-1]
print('Nome Completo: {}'.format(nomeCompleto.split()))
print('Primeiro nome: {}'.format(primeiroNome))
print('Último nome: {} '.format(ultimoNome))