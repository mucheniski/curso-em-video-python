# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

reta1 = int(input('Informe o tamanho da primeira reta: '))
reta2 = int(input('Informe o tamanho da segunda reta: '))
reta3 = int(input('Informe o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores podem formar um triângulo!')

    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os valores não podem formar um triângulo!')