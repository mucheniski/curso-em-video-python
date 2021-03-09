numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
palavra = input('Informe uma palavra: ')
print('Numeros informados {} e {}'.format(numero1, numero2))

soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2
divisaoInteira = numero1 // numero2
restoDaDivisao = numero1 % numero2
potencia = pow(numero1, numero2)
raizQuadrada = potencia**(1/2)
raizCubica = potencia**(1/3)
print('')
print(' a some é {}\n a subtração é {}\n a divisao é {}\n a multiplicação é {}'.format(soma, subtracao, divisao, multiplicacao))
print(' a divisao inteira é {}\n o resto da divisao é {}'.format(divisaoInteira, restoDaDivisao))
print(' a potência é {}\n a raiz quadrada é {}\n a raiz cúbica é {}'.format(potencia, raizQuadrada, raizCubica))

print('='*50)
print('a palavra digitada foi {}'.format(palavra))

print('{} 5 vezes'.format(palavra*5))
print('{:20}| com 20 caracteres'.format(palavra))
print('{:>20}| alinhada a direita com 20 caracteres'.format(palavra))
print('{:<20}| alinhada a esquerda com 20 caracteres'.format(palavra))
print('{:^20} centralizado com 20 caracteres'.format(palavra))
print('{:*^20} centralizado com 20 caracteres e preenchido'.format(palavra))