# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

posicao = int(input('Informe a posição do número: '))

while True:
    if posicao < 0 or posicao > 5:
        posicao = int(input('Precisa ser entre 0 e 5, informe a posição: '))
    else:
        break

print(numerosPorExtenso[posicao])
