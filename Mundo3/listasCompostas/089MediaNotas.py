# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
turma = list()
alunosENotas = list()
boletim = list()
boletims = list()

while True:
    nome = str(input('Informe o nome: '))
    alunosENotas.append(nome)

    nota1 = float(input('Informe a nota1: '))
    alunosENotas.append(nota1)

    nota2 = float(input('Informe a nota2: '))
    alunosENotas.append(nota2)

    turma.append(alunosENotas[:])

    alunosENotas.clear()

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break
print('Fim do programa')
print(turma)

# turma = [['Diego', 10, 8], ['Bruna', 10, 10]]

for aluno in turma:
    print(aluno[0])
    nome = aluno[0]
    boletim.append(nome)

    media = (aluno[1] + aluno[2]) / 2
    boletim.append(media)

    boletims.append(boletim[:])
    boletim.clear()

print(f'Médias: {boletims}')

print('-'*100)
numero = int(input('Informe o número do aluno que deseja mostrar a nota: '))
print(boletims[numero])
