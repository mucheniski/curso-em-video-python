# Exercício Python 040: Crie um programa que leia duas notas de um aluno e
# calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO
nota1 = float(input('Nota1 '))
nota2 = float(input('Nota2 '))
media = (nota1 + nota2) / 2
print('Sua média é de {}'.format(media))

if media < 5.0:
    print('\033[1;31m REPROVADO \033[m')
elif media >= 7.0:
    print('\033[1;32m APROVADO \033[m')
else:
    print('\033[1;33m RECUPERAÇÃO \033[m')