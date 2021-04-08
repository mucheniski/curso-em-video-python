# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

qtdePessoasMaisDe18 = qtdeHomens = qtdeMulheresMenosDe20 = 0
while True:

    print('='*100)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo M|F: ')).strip().upper()[0]

    if idade > 18:
        qtdePessoasMaisDe18 += 1
    if sexo == 'M':
        qtdeHomens += 1
    if sexo == 'F' and idade < 20:
        qtdeMulheresMenosDe20 += 1

    opcao = str(input('Deseja continuar? S|N ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'quantas pessoas tem mais de 18 anos {qtdePessoasMaisDe18}')
print(f'quantos homens foram cadastrados {qtdeHomens}')
print(f'quantas mulheres tem menos de 20 anos {qtdeMulheresMenosDe20}')