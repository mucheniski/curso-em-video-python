# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = random.choice(listaAlunos)
print('O aluno escolhido foi {}'.format(alunoEscolhido))