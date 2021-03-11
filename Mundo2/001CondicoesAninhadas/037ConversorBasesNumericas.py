# Exercício Python 37: Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Informe um número inteiro: '))
print('''Qual a base de conversão? 
1 - Binario 
2 - Octal
3 - Hexadecimal ''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('{} em Binário é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} em Octal é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} em Hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opção {} inválida!'.format(opcao))