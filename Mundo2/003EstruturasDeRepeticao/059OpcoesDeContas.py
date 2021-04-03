# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
opcao = 0
maior = 0
menor = 0
iguais = 'Os valores são iguais'

while opcao != 5:

    print('=========================: \n'
          '1 - Somar \n'
          '2 - Multiplicar \n'
          '3 - Maior \n'
          '4 - novos números \n'
          '5 - Sair do programa \n')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        resultado = valor1 + valor2
        print('Soma de {} + {} = {}'.format(valor1, valor2, resultado))
    elif opcao == 2:
        resultado = valor1 * valor2
        print('Multiplicação de {} X {} = {}'.format(valor1, valor2, resultado))
    elif opcao == 3:
        if valor1 > valor2:
            print('Maior valor {}'.format(valor1))
        elif valor2 > valor1:
            print('Maior valor {}'.format(valor2))
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        valor1 = int(input('Informe o novo primeiro valor: '))
        valor2 = int(input('Informe o novo segundo valor: '))
    elif opcao == 5:
        print('Saiu do programa')
    else:
        print('Opção inválida, tente novamente')

print('Volte sempre!')



