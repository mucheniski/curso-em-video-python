# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

import random
qtdeVitorias = 0

while True:
    numeroComputador = random.randint(0,10)
    print(f'Valor do computador {numeroComputador}')

    opcao = str(input('Voce escolhe Par(P) ou Impar(I)?: ')).strip().upper()[0]
    numeroJogador = int(input('Digite um número: '))

    resultado = numeroJogador + numeroComputador
    if resultado % 2 == 0:
        print('Deu par!')
        if opcao == 'P':
            print('Você ganhou!')
            qtdeVitorias += 1
        else:
            print('Você perdeu!')
            break
    else:
        print('Deu impar!')
        if opcao == 'I':
            print('Você ganhou!')
            qtdeVitorias += 1
        else:
            print('Você perdeu!')
            break
print(f'Quantidade de vitórias consecutivas {qtdeVitorias}')



