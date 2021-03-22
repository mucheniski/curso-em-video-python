# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
numero = int(input('Informe o número para a tabuada: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(numero, i, numero * i))