# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.
# Abaixo de 7 recuperação, abaixo de 5 reprovado
alunos = dict()

alunos['nome'] = str(input('Informe o nome de aluno: '))
alunos['media'] = float(input('Informe a media: '))

print('='*50)
print(f'O nome é igual a {alunos["nome"]}')

if alunos['media'] <= 5.0:
    print('A situação é Reprovado')
elif alunos['media'] <= 7.0:
    print('A situação é Recuperação')
else:
    print('A situação é Aprovado')

