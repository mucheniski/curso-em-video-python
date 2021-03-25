# Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

mediaIdade = 0.0
maiorIdade = 0
nomeHomemMaisVelho = ''
contadorMulheresMenosDe20Anos = 0

for i in range(1,5):
    print('='*50)

    nome = input('Informe o nome da {}ª pessoa: '.format(i))

    idade = int(input('Informe a idade da {}ª pessoa: '.format(i)))
    mediaIdade += idade

    sexo = str(input('Informe o sexo da {}ª pessoa (M ou F): '.format(i))).strip().upper()
    if sexo == 'M':
        if i == 1:
            maiorIdade = idade
            nomeHomemMaisVelho = nome
        if idade > maiorIdade:
            maiorIdade = idade
            nomeHomemMaisVelho = nome
    elif sexo == 'F':
        if idade < 20:
            contadorMulheresMenosDe20Anos += 1;
    else:
        print('Não existe essa opção se sexo')

    print('='*50)
print('A média de idade informada é de {} anos'.format(mediaIdade / 4))

if nomeHomemMaisVelho != '':
    print('O homem mais velho é {} com {} anos '.format(nomeHomemMaisVelho, maiorIdade))
else:
    print('Não existem homens cadastrados!')

print('Foram cadastradas {} mulheres menores de 20 anos!'.format(contadorMulheresMenosDe20Anos))
