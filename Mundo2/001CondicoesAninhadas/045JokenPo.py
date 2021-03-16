import random

# 1-Pedra | 2-Papel | 3-Tesoura

listaOpcoes = ['Pedra', 'Papel', 'Tesoura']
opcaoJogo = random.choice(listaOpcoes)

print('''
1-Pedra
2-Papel
3-Tesoura''')

aux = int(input('Informe a sua opção: '))


opcaoJogador = ''

if aux >= 1 and aux <= 3:
    if aux == 1:
        opcaoJogador = 'Pedra'
    elif aux == 2:
        opcaoJogador = 'Papel'
    elif aux == 3:
        opcaoJogador = 'Tesoura'

    print('Opção do jogador {}'.format(opcaoJogador))
    print('Opção do jogo {}'.format(opcaoJogo))

    if opcaoJogador == opcaoJogo:
        print('Empatou')
    else:
        # papel cobre a pedra
        if opcaoJogador == 'Papel' and opcaoJogo == 'Pedra':
            print('Jogador ganhou')
        # Pedra quebra a tesoura
        elif opcaoJogador == 'Pedra' and opcaoJogo == 'Tesoura':
            print('Jogador ganhou')
        # Tesoura corta o papel
        elif opcaoJogador == 'Tesoura' and opcaoJogo == 'Papel':
            print('Jogador ganhou')
        else:
            print('Jogo ganhou')

else:
    print('Opção inválida')