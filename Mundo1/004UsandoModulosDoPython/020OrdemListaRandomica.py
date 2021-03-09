# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
# o shuffle embaralha os dados da lista
random.shuffle(listaAlunos)
print('A ordem de apresentação será ', listaAlunos)
